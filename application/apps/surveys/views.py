from django.views.generic.base import TemplateView


class SurveyIndexView(TemplateView):
    template_name = "surveys/index.html"
