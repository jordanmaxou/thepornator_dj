from datetime import date

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.glossary.models import Glossary


class GlossarySitemap(Sitemap):
    i18n = True
    protocol = "https"

    def items(self):
        return [
            *list(Glossary.objects.all()),
            {
                "location": reverse("glossary:index"),
                "changefreq": "daily",
                "priority": 0.5,
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
            return 0.5

    def changefreq(self, obj):
        if isinstance(obj, dict):
            return obj["changefreq"]
        return "monthly"
