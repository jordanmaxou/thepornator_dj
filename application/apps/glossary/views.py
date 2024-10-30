from django.views.generic.base import TemplateView


class GlossaryListView(TemplateView):
    template_name = "glossary/list.html"


class GlossaryDetailView(TemplateView):
    template_name = "glossary/detail.html"
