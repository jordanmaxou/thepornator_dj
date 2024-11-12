from django.db import models

# from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify

from .channel import Channel
from .count import Count
from .category import Category


class Video(models.Model):
    slug = models.SlugField(max_length=250, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=800)
    link = models.URLField(max_length=250)
    main_thumb = models.URLField()
    local_main_thumb = models.ImageField(max_length=250, upload_to="img/video")
    publication_date = models.DateField()
    duration = models.DurationField(null=True)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True)
    counts = models.OneToOneField(Count, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
