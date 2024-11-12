from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language


class TrendingSearchesManager(models.Manager):
    def top_15(self):
        return (
            self.filter(lang=get_language())
            .only("slug", "request")
            .order_by("-date", "nb_result")[:15]
        )


class TrendingSearches(models.Model):
    request = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    date = models.DateField()
    nb_result = models.PositiveIntegerField()
    lang = models.CharField(max_length=10)

    objects = TrendingSearchesManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.request.strip())
        super().save(*args, **kwargs)
