from django.db import models


class Note(models.Model):
    funny = models.PositiveIntegerField(default=0)
    sexy = models.PositiveIntegerField(default=0)
    scary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"funny: {self.funny} | sexy: {self.sexy} | scary: {self.scary}"
