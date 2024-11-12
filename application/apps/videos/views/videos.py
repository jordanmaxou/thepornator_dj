from django.views.generic.base import TemplateView


class VideosIndexView(TemplateView):
    template_name = "videos/videos/index.html"


class VideosCategoryView(TemplateView):
    template_name = "videos/videos/category.html"


class VideosChannelView(TemplateView):
    template_name = "videos/videos/channel.html"
