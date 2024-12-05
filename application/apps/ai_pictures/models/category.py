from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    main_image_content = models.ForeignKey(
        "Content", on_delete=models.SET_NULL, null=True, blank=True
    )
    main_video_content = models.ForeignKey(
        "Content",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="video_category_set",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("ai_pictures:category", kwargs={"category": self.slug})
