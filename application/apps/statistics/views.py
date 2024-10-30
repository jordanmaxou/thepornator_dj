from django.views.generic.base import TemplateView


class StatisticsView(TemplateView):
    template_name = "statistics/index.html"
