from os.path import basename
from PIL import Image
import requests
from io import BytesIO

from django.db import models
from django.utils.text import slugify

from .count import Count
from .website import Website
from .category import Category


class TypeOfStatus(models.IntegerChoices):
    OK = 1
    NOT_FOUND = 0
    ERROR = -1


class Profile(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    pseudo = models.CharField(max_length=100)
    photo = models.URLField(max_length=1500)
    description = models.TextField(max_length=500)
    counts = models.OneToOneField(Count, on_delete=models.CASCADE)
    price = models.CharField(max_length=500)
    website = models.ForeignKey(Website, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)
    local_photo = models.ImageField(upload_to="img/photomodels")
    url = models.URLField(max_length=250)
    status = models.SmallIntegerField(choices=TypeOfStatus, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.pseudo)
        super().save(*args, **kwargs)

    def update_counter(self):
        Count.objects.filter(id=self.counts_id).update(clicks=models.F("clicks") + 1)

    def retrieve_image(self):
        if (url := self.photo) and (response := requests.get(url)) and (response.ok()):
            img = Image.open(BytesIO(response.content))
            self.local_photo.save(basename(url), img)
            self.status = TypeOfStatus.OK
        else:
            if response.status_code == 404:
                self.status = TypeOfStatus.NOT_FOUND
            else:
                self.status = TypeOfStatus.ERROR
        self.save(update_fields=["status"])

    def __str__(self):
        return self.slug
