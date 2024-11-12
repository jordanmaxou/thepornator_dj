from django.db import models
from django.utils.text import slugify

from .tag import Tag


class Story(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()
    thumb = models.FileField(upload_to="img/stories")
    author = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
