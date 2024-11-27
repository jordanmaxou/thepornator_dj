from django.db import models
from django.contrib.postgres.fields import ArrayField


class Languages(models.TextChoices):
    FR = "fr"
    EN = "en"


class Devices(models.TextChoices):
    MOBILE = "mobile"
    DESKTOP = "desktop"


class Zones(models.TextChoices):
    TOP = "top"
    BOTTOM = "bottom"
    MIDDLE = "middle"


class Banner(models.Model):
    weight = models.PositiveSmallIntegerField(default=1)
    languages = ArrayField(models.CharField(max_length=2, choices=Languages))
    device = models.CharField(max_length=10, choices=Devices)
    zones = ArrayField(models.CharField(max_length=10, choices=Zones))
    target_url = models.URLField(max_length=250)
    image = models.ImageField(upload_to="img/banners")
    enabled = models.BooleanField(default=True)
