from django.db.models import Avg
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.urls import reverse

from apps.websites.models import Category, Website


class WebsiteCategoryListView(ListView):
    template_name = "websites/category.html"
    context_object_name = "websites"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [{"label": self.category.name}]
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

        radar_data = self.obj.avg_notes_by_theme
        context["radar"] = {
            "data": [
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


class WebsiteSearchView(TemplateView):
    template_name = "websites/search.html"
