from datetime import date

from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _
from django.urls import reverse

from apps.stories.models import Story


class StoryListView(ListView):
    model = Story
    template_name = "stories/list.html"
    context_object_name = "stories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Sex stories"),
            },
        ]
        return context

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(publication_date__lte=date.today())
            .order_by("-publication_date")
        )


class StoryDetailView(DetailView):
    model = Story
    template_name = "stories/detail.html"
    context_object_name = "story"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"label": _("Sex stories"), "link": reverse("stories:index")},
            {"label": self.object.title},
        ]
        return context

    def get_queryset(self):
        return super().get_queryset().filter(publication_date__lte=date.today())
