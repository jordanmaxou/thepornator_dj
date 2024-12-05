from django.db import models


class Languages(models.TextChoices):
    FR = "fr"
    EN = "en"


class TopLink(models.Model):
    label = models.CharField(max_length=100)
    link = models.URLField(max_length=250)
    lang = models.CharField(max_length=2, choices=Languages)
    enabled = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()
