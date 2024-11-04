from django.db import models
from django.utils.text import slugify

from .category import Category
from .deal import Deal


class Website(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=250)
    icon = models.FileField(max_length=150)
    screen = models.FileField(max_length=150)
    is_direct_link = models.BooleanField()
    description = models.TextField(max_length=10000)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    update_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    click = models.PositiveBigIntegerField(default=0)
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, null=True)
    questions = models.ManyToManyField(
        "surveys.Question",
        through="surveys.QuestionWebsite",
        through_fields=("website", "question"),
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.replace(".", ""))
        super().save(*args, **kwargs)
