from datetime import date

from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _
from django.contrib.postgres.search import SearchVector
from django.db.models import Avg, Case, When, F, Q

from apps.websites.models import Website
from apps.porn_models.models import Profile
from apps.trends.models import TrendingSearches


class TrendDetailView(TemplateView):
    template_name = "trends/detail.html"

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get("trend")
        trend = TrendingSearches.objects.filter(slug=slug).first()
        context = super().get_context_data(**kwargs)
        title = _("Trends") + f" {trend.request}"
        context["h1"] = title
        context["breadcrumbs"] = [{"label": title}]
        context["head"] = {
            "title": _("All porn trends %(query)s - The Pornator")
            % {"query": trend.request},
            "description": _(
                "List of porn trends %(query)s by the Pornator visitors over the last 48 hours - The Pornator"
            )
            % {"query": trend.request},
        }

        context["websites"] = (
            Website.objects.filter(
                Q(creation_date__lte=date.today())
                & (Q(end_date__isnull=True) | Q(end_date__gt=date.today()))
            )
            .annotate(
                search=SearchVector("name", "description", "slug"),
                avg_note_update=Avg(
                    Case(
                        When(
                            questionwebsite__note_update__isnull=False,
                            then=F("questionwebsite__note_update"),
                        ),
                        default=F("questionwebsite__note_init"),
                    )
                ),
            )
            .filter(search=trend.request)
        )

        context["profiles"] = Profile.objects.annotate(
            search=SearchVector(
                "pseudo", "description", "categories__name", "website__name"
            )
        ).filter(search=trend.request)

        context["result_nb"] = context["websites"].count() + context["profiles"].count()

        return context
