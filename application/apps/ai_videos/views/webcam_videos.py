from django.views.generic.base import TemplateView


class WebcamVideosIndexView(TemplateView):
    template_name = "ai_videos/webcamvideos/index.html"


class WebcamVideosContentView(TemplateView):
    template_name = "ai_videos/webcamvideos/content.html"
