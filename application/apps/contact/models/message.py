from django.db import models
from django.utils import timezone


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} ({self.name}): {self.subject}"
