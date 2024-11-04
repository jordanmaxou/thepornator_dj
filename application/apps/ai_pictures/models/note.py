from django.db import models


class Note(models.Model):
    funny = models.PositiveIntegerField(default=0)
    sexy = models.PositiveIntegerField(default=0)
    scary = models.PositiveIntegerField(default=0)
