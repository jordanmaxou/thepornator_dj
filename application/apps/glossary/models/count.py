from django.db import models


class Count(models.Model):
    up = models.PositiveIntegerField(default=0)
    down = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"up : {self.up} | down: {self.down}"
