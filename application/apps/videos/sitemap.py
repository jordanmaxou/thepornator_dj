from datetime import date

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.videos.models import Category, Channel


class VideosSitemap(Sitemap):
    i18n = True
    protocol = "https"

    def items(self):
        return [
            *list(Category.objects.all()),
            *list(Channel.objects.all()),
            {
                "location": reverse("videos:videos-index"),
                "changefreq": "daily",
                "priority": 0.8,
                "lastmod": date.today(),
            },
        ]

    def lastmod(self, obj):
        if hasattr(obj, "last_update"):
            return obj.last_update.date()
        elif isinstance(obj, dict):
            return obj["lastmod"]
        return date.today()

    def location(self, obj):
        if isinstance(obj, dict):
            return obj["location"]
        else:
            return super().location(obj)

    def priority(self, obj):
        if isinstance(obj, dict):
            return obj["priority"]
        else:
            return 1

    def changefreq(self, obj):
        if isinstance(obj, dict):
            return obj["changefreq"]
        return "weekly"


class WebcamvideosSitemap(Sitemap):
    i18n = True
    protocol = "https"
    priority = "daily"
    changefreq = 0.5

    def items(self):
        return [{"location": reverse("videos:webcam-videos-index")}]

    def lastmod(self, _obj):
        return date.today()

    def location(self, obj):
        return obj["location"]
