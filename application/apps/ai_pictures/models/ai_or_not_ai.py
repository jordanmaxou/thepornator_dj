from django.db import models


class AiOrNotAi(models.Model):
    score = models.PositiveIntegerField(default=0)
    ip = models.CharField(max_length=50)
    date = models.DateTimeField()
