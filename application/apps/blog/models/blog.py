from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()
    thumb = models.FileField()
    author = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
