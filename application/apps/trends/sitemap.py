from datetime import date

from django.contrib.sitemaps import Sitemap

from apps.trends.models import TrendingSearches


class TrendsSitemap(Sitemap):
    i18n = True
    protocol = "https"
    priority = 0.2
    changefreq = "monthly"

    def items(self):
        return TrendingSearches.objects.all()

    def lastmod(self, obj):
        return date.today()
