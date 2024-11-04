from django.db import models


class Count(models.Model):
    clicks = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    photos = models.PositiveIntegerField(default=0)
    videos = models.PositiveIntegerField(default=0)
    posts = models.PositiveIntegerField(default=0)
