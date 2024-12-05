from datetime import date
from os.path import basename
from PIL import Image
import requests
from io import BytesIO

from django.db import models
from django.urls import reverse

from .note import Note
from .country import Country
from .category import Category
from apps.websites.models import Website
from apps.ai_pictures.utils import upload_to_according_to_type


class TypeOfContent(models.TextChoices):
    IMAGE = "image"
    VIDEO = "video"


class TypeOfStatus(models.IntegerChoices):
    OK = 1
    NOT_FOUND = 0
    ERROR = -1


class Content(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TypeOfContent)
    slug = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateField()
    note = models.OneToOneField(Note, on_delete=models.CASCADE)
    source = models.ForeignKey(Website, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(
        max_length=250, upload_to=upload_to_according_to_type, null=True, blank=True
    )
    external_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(choices=TypeOfStatus, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["source"]),
            models.Index(fields=["publication_date"]),
            models.Index(fields=["type"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.type == TypeOfContent.IMAGE:
            return reverse("ai_pictures:content", kwargs={"slug": self.slug})
        elif self.type == TypeOfContent.VIDEO:
            return reverse(
                "ai_pictures:ai-porn-videos-content", kwargs={"slug": self.slug}
            )

    def retrieve_image(self):
        max_size = (512, 512)
        if (
            (url := self.external_url)
            and (response := requests.get(url))
            and (response.ok())
        ):
            img = Image.open(BytesIO(response.content))
            if img.height > max_size[1] or img.width > max_size[0]:
                img.thumbnail(max_size, Image.ANTIALIAS)
            self.image.save(basename(url), img)

    @property
    def selected_categories(self):
        selected_categories = list(self.categories.values_list("id", flat=True))
        return (
            self.categories.model.objects.annotate(
                selected=models.Case(
                    models.When(id__in=selected_categories, then=True),
                    default=False,
                    output_field=models.BooleanField(),
                )
            )
            .order_by("name")
            .values("id", "name", "selected")
        )

    @property
    def selected_countries(self):
        if self.country:
            return self.country.__class__.objects.annotate(
                selected=models.Case(
                    models.When(id=self.country.id, then=True),
                    default=False,
                    output_field=models.BooleanField(),
                )
            )
        else:
            return Country.objects.annotate(
                selected=models.Value(False, models.BooleanField())
            )

    def next_content(self, type: TypeOfContent):
        return (
            self.__class__.objects.filter(
                type=type,
                publication_date__lte=date.today(),
                categories__in=self.categories.all(),
            )
            .order_by("?")
            .first()
        )
