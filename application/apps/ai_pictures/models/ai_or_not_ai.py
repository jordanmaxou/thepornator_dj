from django.db import models

from apps.ai_pictures.utils import upload_to_according_to_fake_of_real


class AiOrNotAiScore(models.Model):
    score = models.PositiveIntegerField(default=0)
    ip = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)


class AiOrNotAiImage(models.Model):
    picture = models.ImageField(upload_to=upload_to_according_to_fake_of_real)
    is_real = models.BooleanField()
    enabled = models.BooleanField()
