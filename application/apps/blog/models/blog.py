from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Blog(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()
    thumb = models.FileField(upload_to="img/blog")
    author = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:content", kwargs={"slug": self.slug})

    def __str__(self):
        return self.slug
