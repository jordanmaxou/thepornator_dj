from datetime import date

from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _
from django.urls import reverse

from apps.scripts.models import Content


class ScriptListView(ListView):
    model = Content
    template_name = "scripts/list.html"
    context_object_name = "scripts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Porn scripts"),
            },
        ]
        context["head"] = {
            "title": _("Porn movies script in English - The Pornator"),
            "description": _(
                "Find a porn movie from its script. For the first time, here is the scripts of real porn movies in English."
            ),
        }
        return context

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(publication_date__lte=date.today())
            .order_by("-publication_date")
        )


class ScriptDetailView(DetailView):
    model = Content
    template_name = "scripts/detail.html"
    context_object_name = "script"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"label": _("Porn scripts"), "link": reverse("scripts:index")},
            {"label": self.object.title},
        ]
        context["head"] = {
            "title": _("Read script of porn movie %(title)s")
            % {"title": self.object.title},
            "description": f"{self.object.text[:140]}{'...' if len(self.object.text) > 140 else ''}",
        }
        return context

    def get_queryset(self):
        return super().get_queryset().filter(publication_date__lte=date.today())
