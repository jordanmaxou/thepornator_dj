from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


class CategoryManager(models.Manager):
    def flatten_terms(self):
        objs = {
            row["id"]: [row["name_fr"], row["name_en"], *row["synonyms"]]
            for row in self.values("id", "name_fr", "name_en", "synonyms")
        }
        words_dict = {}
        for id, words in objs.items():
            for word in words:
                words_dict[word.lower()] = id

        return words_dict


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    slug = models.SlugField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    main_profile = models.ForeignKey(
        "Profile", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    synonyms = ArrayField(models.CharField(max_length=50), default=list)

    objects = CategoryManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("porn_models:category", kwargs={"category": self.slug})

    def __str__(self):
        return self.slug
