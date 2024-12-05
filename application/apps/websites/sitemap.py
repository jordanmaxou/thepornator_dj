from datetime import date

from django.contrib.sitemaps import Sitemap
from apps.websites.models import Website, Category


class WebsiteSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    i18n = True
    protocol = "https"

    def items(self):
        return list(Website.objects.filter(end_date__gte=date.today())) + list(
            Category.objects.all()
        )

    def lastmod(self, obj):
        if isinstance(obj, Website):
            return obj.update_date
        else:
            return date.today()
