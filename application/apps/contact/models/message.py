from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
