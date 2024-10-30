from django.views.generic.base import TemplateView


class WebsiteCategoryListView(TemplateView):
    template_name = "websites/category.html"


class WebsiteSiteDetailView(TemplateView):
    template_name = "websites/site.html"
