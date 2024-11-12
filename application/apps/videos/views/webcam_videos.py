from django.views.generic.base import TemplateView


class WebcamVideosIndexView(TemplateView):
    template_name = "videos/webcamvideos/index.html"


class WebcamVideosContentView(TemplateView):
    template_name = "videos/webcamvideos/content.html"
