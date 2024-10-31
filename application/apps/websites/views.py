from django.views.generic.base import TemplateView


class WebsiteCategoryListView(TemplateView):
    template_name = "websites/category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [{"label": "Générateur porno IA"}]
        return context


class WebsiteSiteDetailView(TemplateView):
    template_name = "websites/site.html"
