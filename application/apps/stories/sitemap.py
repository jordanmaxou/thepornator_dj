from datetime import date

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.stories.models import Story


class StorySitemap(Sitemap):
    i18n = True
    protocol = "https"

    def items(self):
        return [
            *list(Story.objects.all()),
            {
                "location": reverse("stories:index"),
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
