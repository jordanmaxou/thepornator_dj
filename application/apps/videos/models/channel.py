from django.db import models
from django.utils.text import slugify


class Channel(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to="img/logosites")
    link = models.URLField()
    description = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
