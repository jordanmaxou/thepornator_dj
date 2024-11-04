from django.db import models
from apps.websites.models import Website
from .question import Question


class Survey(models.Model):
    hash = models.CharField(max_length=255)
    update_date = models.DateField()
    website = models.ForeignKey(Website, on_delete=models.SET_NULL, null=True)
    is_validated = models.BooleanField(null=True, blank=True)
    ip = models.CharField(max_length=30)
    ua = models.CharField(255)
    duration = models.DurationField()
    questions = models.ManyToManyField(
        Question,
        through="QuestionSurvey",
        through_fields=("survey", "question"),
    )
