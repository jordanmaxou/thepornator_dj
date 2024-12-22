from os.path import basename
from PIL import Image
import requests
from io import BytesIO

from django.db import models
from django.utils.text import slugify

from .channel import Channel
from .count import Count
from .category import Category


class TypeOfStatus(models.IntegerChoices):
    OK = 1
    NOT_FOUND = 0
    ERROR = -1


class Video(models.Model):
    slug = models.SlugField(max_length=250, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=800)
    link = models.URLField(max_length=250)
    main_thumb = models.URLField()
    local_main_thumb = models.ImageField(max_length=250, upload_to="img/video")
    publication_date = models.DateField()
    duration = models.DurationField(null=True)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True)
    counts = models.OneToOneField(Count, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)
    status = models.SmallIntegerField(choices=TypeOfStatus, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def update_counter(self):
        Count.objects.filter(id=self.counts_id).update(clicks=models.F("clicks") + 1)

    def vote_up(self):
        Count.objects.filter(id=self.counts_id).update(up=models.F("up") + 1)

    def vote_down(self):
        Count.objects.filter(id=self.counts_id).update(down=models.F("down") + 1)

    def __str__(self):
        return self.slug

    def retrieve_image(self):
        max_size = (512, 512)
        if (
            (url := self.main_thumb)
            and (response := requests.get(url))
            and (response.ok())
        ):
            img = Image.open(BytesIO(response.content))
            if img.height > max_size[1] or img.width > max_size[0]:
                img.thumbnail(max_size, Image.ANTIALIAS)
            self.local_main_thumb.save(basename(url), img)
            self.status = TypeOfStatus.OK
        else:
            if response.status_code == 404:
                self.status = TypeOfStatus.NOT_FOUND
            else:
                self.status = TypeOfStatus.ERROR
        self.save(update_fields=["status"])
