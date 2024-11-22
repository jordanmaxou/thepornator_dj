from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    main_profile = models.ForeignKey(
        "Profile", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
