from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language
from datetime import timedelta


class TrendingSearchesManager(models.Manager):
    def top_15(self):
        most_recent_date = self.all().order_by("-date").first().date
        four_days_ago = most_recent_date - timedelta(days=4)
        return (
            self.filter(lang=get_language(), date__gte=four_days_ago)
            .exclude(slug="")
            .values("slug")
            .annotate(nb=models.Count("id"))
            .order_by("-nb")
            .values("date", "lang", "nb", "request", "slug")
        )


class TrendingSearches(models.Model):
    request = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    date = models.DateField(auto_now_add=True)
    nb_result = models.PositiveIntegerField()
    lang = models.CharField(max_length=10)

    objects = TrendingSearchesManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.request.strip())
        super().save(*args, **kwargs)
