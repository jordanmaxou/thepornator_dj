from django.db import models

from .survey import Survey
from .question import Question


class QuestionSurvey(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    note = models.PositiveIntegerField(default=0)
