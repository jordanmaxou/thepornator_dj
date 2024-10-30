from django.views.generic.base import TemplateView


class AiPornVideosIndexView(TemplateView):
    template_name = "ai_videos/aipornvideos/index.html"


class AiPornVideosCategoryView(TemplateView):
    template_name = "ai_videos/aipornvideos/category.html"


class AiPornVideosSourceView(TemplateView):
    template_name = "ai_videos/aipornvideos/source.html"


class AiPornVideosContentView(TemplateView):
    template_name = "ai_videos/aipornvideos/content.html"
