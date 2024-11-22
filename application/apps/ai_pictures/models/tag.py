from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    lang = models.CharField(max_length=2)
    contents = models.ManyToManyField(to="ai_pictures.content")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name).replace("-", "")
        super().save(*args, **kwargs)
