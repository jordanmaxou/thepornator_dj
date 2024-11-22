from datetime import date

from django.db.models.functions import Substr
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import get_language
from apps.glossary.models import Glossary


class GlossaryListView(ListView):
    template_name = "glossary/list.html"
    context_object_name = "terms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Porn dictionnary"),
            },
        ]
        context["positions"] = Glossary.objects.filter(
            (Q(lang=get_language()) | Q(lang__isnull=True))
            & Q(type="position")
            & Q(publication_date__lte=date.today())
        ).order_by("name")

        return context

    def get_queryset(self):
        return Glossary.objects.filter(
            (Q(lang=get_language()) | Q(lang__isnull=True))
            & Q(type__in=["vocabulary", "acronyme"])
            & Q(publication_date__lte=date.today())
        ).annotate(
            first_letter=Substr("name", 1, 1),
        )


class GlossaryDetailView(DetailView):
    model = Glossary
    template_name = "glossary/detail.html"
    context_object_name = "term"
    slug_url_kwarg = "term"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"label": _("Porn dictionnary"), "link": reverse("glossary:index")},
            {"label": self.object.name},
        ]
        context["related_contents"] = (
            self.model.objects.exclude(id=self.object.id)
            .filter(
                (Q(lang=get_language()) | Q(lang__isnull=True))
                & Q(type=self.object.type)
                & Q(publication_date__lte=date.today())
            )
            .order_by("?")[: 8 if self.object.type == "acronyme" else 4]
        )
        return context

    def get_queryset(self):
        return self.model.objects.filter(
            (Q(lang=get_language()) | Q(lang__isnull=True))
            & Q(publication_date__lte=date.today())
        )
