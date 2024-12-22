from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

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

    def get_absolute_url(self):
        return reverse("videos:videos-category", kwargs={"category": self.slug})

    def __str__(self):
        return self.slug
