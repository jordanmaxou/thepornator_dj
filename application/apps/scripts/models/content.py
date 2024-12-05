from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Content(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    studio = models.CharField(max_length=100)
    link = models.URLField(max_length=250)
    thumb = models.FileField(upload_to="img/script")
    text = models.TextField()
    publication_date = models.DateField()
    lang = models.CharField(max_length=3)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("scripts:content", kwargs={"slug": self.slug})
