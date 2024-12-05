from datetime import date
from django.db.models import Avg, Case, When, F, Q
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.contrib.postgres.search import SearchVector
from django.urls import reverse
from django.utils.translation import get_language
from django.conf import settings

from apps.websites.models import Category, Website
from apps.trends.models import TrendingSearches


class WebsiteCategoryListView(ListView):
    template_name = "websites/category.html"
    context_object_name = "websites"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [{"label": self.category.name}]
        context["head"] = {
            "title": _("Ranking of %(category)s - ThePornator")
            % {"category": self.category.name},
            "description": _(
                "Check out the ultimate list of %(category)s now on thePornator!"
            )
            % {"category": self.category.name},
        }
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["category"])
        return (
            Website.objects.filter(category=self.category)
            .annotate(
                avg_note_update=Avg("questionwebsite__note_update"),
            )
            .select_related("category")
            .order_by("-avg_note_update")
        )


class WebsiteSiteDetailView(DetailView):
    template_name = "websites/site.html"
    model = Website
    context_object_name = "website"
    slug_url_kwarg = "website"

    def get_object(self, queryset=None):
        self.obj = super(WebsiteSiteDetailView, self).get_object(queryset=queryset)

        return self.obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": self.obj.category.name,
                "link": reverse(
                    "websites:category", kwargs={"category": self.obj.category.slug}
                ),
            },
            {"label": self.obj.name},
        ]
        context["page_type"] = "website-detail"
        context["head"] = {
            "title": _("Watch review of porn site %(site)s - ThePornator")
            % {"site": self.obj.name},
            "description": _(
                "A review of the porn site %(site)s that is objective and based on different axes of comparison. Trust the Pornator!"
            )
            % {"site": self.obj.name},
        }
        radar_data = self.obj.avg_notes_by_theme
        context["radar"] = {
            "datasets": [
                {
                    "label": self.obj.name,
                    "data": [
                        radar_data["Quantity"],
                        radar_data["Quality"],
                        radar_data["Security"],
                        radar_data["Navigation"],
                    ],
                    "backgroundColor": ["rgba(255, 99, 132, 0.2)"],
                    "borderColor": ["rgba(255, 99, 132, 0.2)"],
                    "borderWidth": 1,
                }
            ],
            "labels": [_("Quantity"), _("Quality"), _("Security"), _("Navigation")],
        }

        context["related_websites"] = (
            Website.objects.filter(category=self.obj.category)
            .exclude(id=self.obj.id)
            .annotate(
                avg_note_update=Avg("questionwebsite__note_update"),
            )
            .select_related("category")
            .order_by("-avg_note_update")
        )

        return context


class WebsiteSearchView(ListView):
    model = Website
    context_object_name = "websites"
    template_name = "websites/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["head"] = {
            "title": _("All porn sites %(criterias)s - The Pornator")
            % {"criterias": self.query},
            "description": _(
                "List of sites %(criterias)s among all the best web porn on the web - The Pornator"
            )
            % {"criterias": self.query},
        }
        context["breadcrumbs"] = [{"label": _("Results")}]
        base_url = (
            reverse("websites:search")
            + f"?query={self.query}&rating={self.rating}&category={self.category}"
        )
        context["sort_urls"] = {
            "newest": f"{base_url}&sort=newest",
            "rated": f"{base_url}&sort=rated",
        }
        context["current_sort"] = self.sort

        if (
            self.queryset.count() > 0
            and (query := self.query.strip())
            and len(query) > 0
        ):
            TrendingSearches.objects.create(
                request=self.query, lang=get_language(), nb_result=self.queryset.count()
            )
        return context

    def get_queryset(self):
        self.query = self.request.GET.get("query")
        if self.query in settings.WORD_BLACK_LIST:
            return super().get_queryset().none()
        self.rating = self.request.GET.get("rating")
        self.category = self.request.GET.get("category")
        self.sort = self.request.GET.get("sort")
        qs = (
            super()
            .get_queryset()
            .filter(
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
        )
        if self.query:
            qs = qs.filter(search=self.query)
        if self.rating and (rating := int(self.rating)):
            qs = qs.filter(avg_note_update__range=(rating, rating + 1))
        if self.category:
            qs = qs.filter(category__slug=self.category)

        if self.sort:
            if self.sort == "newest":
                qs = qs.order_by("-creation_date")
            elif self.sort == "rated":
                qs = qs.order_by("-avg_note_update")
        self.queryset = qs
        return qs
