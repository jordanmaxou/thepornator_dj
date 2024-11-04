from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    position = models.SmallIntegerField()
    icon = models.FileField(max_length=150, upload_to="img/iconcategories")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
