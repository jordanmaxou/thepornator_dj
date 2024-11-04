from django.db import models

from .question import Question
from apps.websites.models import Website


class QuestionWebsite(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    note_init = models.PositiveIntegerField(default=0)
    note_update = models.PositiveIntegerField(default=0)
    note_nb = models.PositiveIntegerField(default=0)
