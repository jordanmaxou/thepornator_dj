from django.views.generic.base import TemplateView


class AiPornIndexView(TemplateView):
    template_name = "ai_pictures/index.html"


class AiPornCategoryView(TemplateView):
    template_name = "ai_pictures/category.html"


class AiPornCountriesView(TemplateView):
    template_name = "ai_pictures/countries.html"


class AiPornCountryView(TemplateView):
    template_name = "ai_pictures/country.html"


class AiPornTagsView(TemplateView):
    template_name = "ai_pictures/tags.html"


class AiPornTagView(TemplateView):
    template_name = "ai_pictures/tag.html"


class AiPornSourceView(TemplateView):
    template_name = "ai_pictures/source.html"


class AiPornAiOrNotAiView(TemplateView):
    template_name = "ai_pictures/aiornotai.html"


class AiPornContentView(TemplateView):
    template_name = "ai_pictures/content.html"
