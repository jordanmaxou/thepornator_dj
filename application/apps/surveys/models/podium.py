from django.db import models

from apps.websites.models import Website


class Podium(models.Model):
    first = models.ForeignKey(Website, on_delete=models.SET_NULL, null=True, blank=True)
    second = models.ForeignKey(
        Website, on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    third = models.ForeignKey(
        Website, on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
