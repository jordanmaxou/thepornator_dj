from django.db import models

from .theme import Theme


class Question(models.Model):
    sentence = models.CharField(max_length=150)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
