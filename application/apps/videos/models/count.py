from django.db import models


class Count(models.Model):
    up = models.PositiveIntegerField(default=0)
    down = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.up} | {self.down} | {self.clicks}"
