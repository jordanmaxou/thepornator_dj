from datetime import date
import json

from django.db.models.functions import Substr
from django.views.generic import ListView, DetailView, View
from django.utils.translation import gettext as _
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import get_language
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

from apps.glossary.models import Glossary, TypeOfTerm


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
        context["head"] = {
            "title": _("Porn dictionnary with sexual vocabulary - ThePornator"),
            "description": _(
                "A complete NSFW porn dictionary / search engine porn terms with acronyms, glossary, lingo, codes, terminology and illustrated with images, gifs or videos"
            ),
        }
        context["positions"] = Glossary.objects.filter(
            (Q(lang=get_language()) | Q(lang__isnull=True))
            & Q(type=TypeOfTerm.POSITION)
            & Q(publication_date__lte=date.today())
        ).order_by("name")

        return context

    def get_queryset(self):
        return Glossary.objects.filter(
            (Q(lang=get_language()) | Q(lang__isnull=True))
            & Q(type__in=[TypeOfTerm.VOCABULARY, TypeOfTerm.ACRONYM])
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
        context["page_type"] = "glossary"
        context["head"] = {
            "title": _(
                "Definition %(type)s %(term)s - Sexual vocabulary - The Pornator"
            )
            % {
                "term": self.object.name,
                "type": "Term"
                if self.object.type == "vocabulary"
                else self.object.type.capitalize(),
            },
            "description": f"{self.object.definition[:140]}{'...' if len(self.object.definition) > 140 else '' }",
        }
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


class GlossaryVoteView(View):
    def post(self, request, term):
        term = get_object_or_404(
            Glossary, Q(slug=term) & (Q(lang=get_language()) | Q(lang__isnull=True))
        )
        data = json.loads(request.body)
        if (type_vote := data.get("type")) and type_vote in ["up", "down"]:
            getattr(term, type_vote)()
            term.count.refresh_from_db()
            return JsonResponse({"up": term.count.up, "down": term.count.down})
        return HttpResponse(status=400)
