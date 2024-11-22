from math import sqrt, pow

from django.db import models
from apps.websites.models import Website
from .question import Question
from .podium import Podium


class Survey(models.Model):
    user_daily_fingerprint = models.CharField(max_length=255, unique=True)
    creation_date = models.DateField(auto_now_add=True)
    is_valid = models.BooleanField(default=False)
    duration = models.DurationField()
    questions = models.ManyToManyField(
        Question,
        through="QuestionSurvey",
        through_fields=("survey", "question"),
    )
    selected_websites = models.OneToOneField(
        Podium, on_delete=models.CASCADE, null=True
    )

    def get_notes(self):
        return {
            d["question"]: d["note"]
            for d in self.questions.through.objects.values("question", "note")
        }

    def get_nearest_websites(self):
        notes_by_websites = Website.objects.get_notes_by_websites()
        current_survey_notes = self.get_notes()
        distances = {}
        for site_id, notes in notes_by_websites.items():
            distances[site_id] = sqrt(
                sum(
                    [
                        pow(current_survey_notes[question_id] - note, 2)
                        for question_id, note in notes.items()
                    ]
                )
            )

        website_ids = sorted(distances, key=distances.get)[:3]

        return [Website.objects.get(id=website_id) for website_id in website_ids]

    @property
    def notes_by_theme(self) -> dict:
        return {
            item["question__theme__name"]: round(item["avg_note"], 2)
            for item in (
                self.questions.through.objects.prefetch_related(
                    "question", "question__theme"
                )
                .filter(survey_id=self.id)
                .values("question__theme__name")
                .annotate(avg_note=models.Avg("note"))
            )
        }
