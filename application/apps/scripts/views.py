from django.views.generic.base import TemplateView


class ScriptListView(TemplateView):
    template_name = "scripts/list.html"


class ScriptDetailView(TemplateView):
    template_name = "scripts/detail.html"
