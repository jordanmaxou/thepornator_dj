from django.views.generic.base import TemplateView


class VideosIndexView(TemplateView):
    template_name = "ai_videos/videos/index.html"


class VideosCategoryView(TemplateView):
    template_name = "ai_videos/videos/category.html"


class VideosChannelView(TemplateView):
    template_name = "ai_videos/videos/channel.html"
