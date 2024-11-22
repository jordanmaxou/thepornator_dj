from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    main_content = models.ForeignKey(
        "Video", on_delete=models.SET_NULL, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
