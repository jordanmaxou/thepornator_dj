from django.db import models
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    icon = models.TextField(max_length=20000)
    main_content = models.ForeignKey(
        "Content", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
