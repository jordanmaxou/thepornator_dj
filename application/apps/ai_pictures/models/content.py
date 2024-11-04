from django.db import models
from .note import Note
from .country import Country
from .category import Category
from apps.websites.models import Website


class Content(models.Model):
    class TypeOfContent(models.TextChoices):
        IMAGE = "image"
        VIDEO = "video"

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TypeOfContent)
    code = models.CharField(max_length=100)
    publication_date = models.DateField()
    note = models.OneToOneField(Note, on_delete=models.CASCADE)
    source = models.ForeignKey(Website, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["source"]),
            models.Index(fields=["publication_date"]),
            models.Index(fields=["type"]),
        ]
