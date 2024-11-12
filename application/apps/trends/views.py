from django.views.generic.base import TemplateView


class TrendDetailView(TemplateView):
    template_name = "trends/detail.html"
