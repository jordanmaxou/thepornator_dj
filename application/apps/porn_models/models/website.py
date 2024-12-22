from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Website(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    image = models.ImageField(upload_to="img/logomodelsites")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("porn_models:website", kwargs={"website": self.slug})

    def __str__(self):
        return self.slug
