from datetime import date
from random import randint

from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _
from django.contrib.postgres.search import SearchVector
from django.db.models import Avg, Case, When, F, Q

from apps.websites.models import Website
from apps.porn_models.models import Profile
from apps.trends.models import TrendingSearches
from apps.porn_models.utils import get_fake_model_profiles


class TrendDetailView(TemplateView):
    template_name = "trends/detail.html"
    fake_profiles_positions = [0, 2, 4, 6, 8]

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

        profiles = list(
            Profile.objects.annotate(
                search=SearchVector(
                    "pseudo", "description", "categories__name", "website__name"
                )
            )
            .filter(search=trend.request)
            .distinct("id")
        )
        fake_profiles = get_fake_model_profiles("onlyfans")
        for i in self.fake_profiles_positions:
            if i < len(profiles):
                profiles.insert(
                    i, fake_profiles.pop(randint(0, len(fake_profiles) - 1))
                )
        context["profiles"] = profiles

        context["result_nb"] = context["websites"].count() + len(context["profiles"])

        return context
