from django.db import models
from django.utils.text import slugify

from .count import Count


class Glossary(models.Model):
    slug = models.SlugField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    meaning = models.TextField(max_length=100, null=True)
    definition = models.TextField(max_length=1200)
    picture = models.FileField(upload_to="img/glossary")
    publication_date = models.DateField()
    count = models.OneToOneField(Count, on_delete=models.CASCADE)
    lang = models.CharField(max_length=5, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
