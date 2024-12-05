from datetime import date

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    i18n = True
    protocol = "https"

    def items(self):
        now = date.today()
        return [
            {
                "url_name": "home:home",
                "priority": 1,
                "changefreq": "daily",
                "lastmod": now,
            },
            {
                "url_name": "contact:contact",
                "priority": 0.1,
                "changefreq": "monthly",
                "lastmod": now,
            },
            {
                "url_name": "pages:about",
                "priority": 0.1,
                "changefreq": "monthly",
                "lastmod": now,
            },
        ]

    def location(self, item):
        return reverse(item["url_name"])

    def priority(self, item):
        return item["priority"]

    def changefreq(self, item):
        return item["changefreq"]

    def lastmod(self, item):
        return item["lastmod"]
