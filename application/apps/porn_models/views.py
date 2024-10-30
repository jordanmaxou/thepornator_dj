from django.views.generic.base import TemplateView


class PornModelsIndexView(TemplateView):
    template_name = "porn_models/index.html"


class PornModelsSearchView(TemplateView):
    template_name = "porn_models/search.html"


class PornModelsCategoryView(TemplateView):
    template_name = "porn_models/category.html"


class PornModelsSiteView(TemplateView):
    template_name = "porn_models/site.html"


class PornModelsSiteCategoryView(TemplateView):
    template_name = "porn_models/site-category.html"
