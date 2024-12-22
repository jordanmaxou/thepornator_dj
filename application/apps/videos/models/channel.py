from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Channel(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to="img/logosites")
    link = models.URLField()
    description = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("videos:videos-channel", kwargs={"channel": self.slug})

    def __str__(self):
        return self.slug
