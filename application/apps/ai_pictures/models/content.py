from typing import Optional

from os.path import basename
from PIL import Image
import requests
from io import BytesIO

from django.db import models

from .note import Note
from .country import Country
from .category import Category
from apps.websites.models import Website
from apps.ai_pictures.utils import upload_to_according_to_type


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
    image = models.ImageField(
        max_length=250, upload_to=upload_to_according_to_type, null=True, blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["source"]),
            models.Index(fields=["publication_date"]),
            models.Index(fields=["type"]),
        ]

    def get_image_url(self) -> Optional[str]:
        match self.source.slug:
            case "madeporn" if len(self.code) == 23:
                return f"https://made.porn/600/is/{self.code[9:11]}/{self.code[7:9]}/{self.code}.jpg"
            case "madeporn" if len(self.code) == 22:
                return f"https://made.porn/600/is/{self.code[8:10]}/{self.code[6:8]}/{self.code}.jpg"
            case "pornmake":
                return f"https://cdn.pornmake.ai/static/webp/{self.code}.webp"
            case "pornxai":
                return f"https://cdn1.pornx.ai/{self.code}"
            case "xpicturesio":
                return f"https://x-pictures-back-main.s3.us-east-2.amazonaws.com/media/generate-jobs/{self.code}.jpeg"
            case "pornpen":
                return f"https://cdn.pornpen.ai/{self.code}.jpg"
            case _:
                return None

    def retrieve_image(self):
        max_size = (512, 512)
        if (
            (url := self.get_image_url())
            and (response := requests.get(url))
            and (response.ok())
        ):
            img = Image.open(BytesIO(response.content))
            if img.height > max_size[1] or img.width > max_size[0]:
                img.thumbnail(max_size, Image.ANTIALIAS)
            self.image.save(basename(url), img)
