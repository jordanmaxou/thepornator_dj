from datetime import date

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.porn_models.models import Category, Website


class PornModelSitemap(Sitemap):
    i18n = True
    protocol = "https"

    def items(self):
        categories = list(Category.objects.all())
        websites = list(Website.objects.all())
        objs = [*categories, *websites]
        for website in websites:
            for category in categories:
                objs.append(
                    {
                        "location": reverse(
                            "porn_models:website-category",
                            kwargs={"website": website.slug, "category": category.slug},
                        ),
                        "changefreq": "weekly",
                        "priority": 1,
                        "lastmod": date.today(),
                    }
                )
        return objs + [
            {
                "location": reverse("porn_models:index"),
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
