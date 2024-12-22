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

    def __str__(self):
        items = [
            f"{k}: {v}"
            for k, v in {
                "first": self.first,
                "second": self.second,
                "third": self.third,
            }.items()
            if v is not None
        ]

        return " | ".join(items)
