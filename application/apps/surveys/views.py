import json
from datetime import timedelta

from django.db import transaction
from django.views.generic.base import TemplateView
from django.views.generic import View, DetailView
from django.utils.translation import gettext as _
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.urls import reverse

from apps.surveys.models import Question, Survey, QuestionSurvey, Podium
from libs.request import user_daily_fingerprint


class SurveyIndexView(TemplateView):
    template_name = "surveys/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"label": _("Find my porn")},
        ]
        context["page_type"] = "survey-questions"
        context["head"] = {
            "title": _("Questions to find a porn site"),
            "description": _(
                "Answer the 16 questions to compare your expectations and the characteristics of the porn sites analysed. Answer in 3 minutes!"
            ),
        }

        fingerprint = user_daily_fingerprint(self.request)

        if settings.DEBUG is True:
            context["can_answer"] = True
        else:
            context["can_answer"] = not Survey.objects.filter(
                user_daily_fingerprint=fingerprint
            ).exists()

        context["questions"] = (
            [
                {"id": row.id, "question": row.sentence, "answer": None}
                for row in Question.objects.all().order_by("position")
            ]
            if context["can_answer"]
            else []
        )
        context["fingerprint"] = fingerprint

        return context


class AddSurveyView(View):
    def post(self, request):
        fingerprint = user_daily_fingerprint(self.request)
        data = json.loads(request.body)

        if settings.DEBUG is False:
            if data["duration"] < settings.SURVEY_TIME_THRESHOLD_SECONDS:
                return HttpResponse(status=406)

        if (
            settings.DEBUG is True
            and Survey.objects.filter(user_daily_fingerprint=fingerprint).exists()
        ):
            survey = Survey.objects.get(user_daily_fingerprint=fingerprint)
            survey.questions.clear()
            survey.delete()

        with transaction.atomic():
            survey = Survey.objects.create(
                user_daily_fingerprint=fingerprint,
                duration=timedelta(seconds=data["duration"]),
            )
            survey.questions.through.objects.bulk_create(
                [
                    QuestionSurvey(
                        survey_id=survey.id,
                        question_id=note["id"],
                        note=note["answer"],
                    )
                    for note in data["notes"]
                ]
            )
            first, second, third = survey.get_nearest_websites()
            survey.selected_websites = Podium.objects.create(
                first=first, second=second, third=third
            )
            survey.save()

        return JsonResponse(
            {"redirect_url": reverse("surveys:result", kwargs={"slug": fingerprint})},
            status=201,
        )


class UpdateIsValidSurveyView(View):
    def post(self, request, slug):
        data = json.loads(request.body)
        if (is_valid := data.get("is_valid")) and isinstance(is_valid, bool):
            survey = get_object_or_404(Survey, user_daily_fingerprint=slug)
            with transaction.atomic():
                survey.is_valid = is_valid
                survey.save()
                survey.selected_websites.first.update_notes()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class ResultDetailView(DetailView):
    model = Survey
    template_name = "surveys/result.html"
    slug_field = "user_daily_fingerprint"
    context_object_name = "survey"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"label": _("Survey result")},
        ]
        context["page_type"] = "survey-results"
        context["head"] = {
            "title": _("The right site for you - The Pornator"),
            "description": _(
                "Find out which porn site is best for you based on your answers to the questionnaire - The Pornator"
            ),
        }
        survey_notes = self.object.notes_by_theme
        website_notes = self.object.selected_websites.first.avg_notes_by_theme
        context["radar"] = {
            "labels": ["Quantity", "Quality", "Security", "Navigation"],
            "datasets": [
                {
                    "label": "You",
                    "data": [
                        survey_notes["Quantity"],
                        survey_notes["Quality"],
                        survey_notes["Security"],
                        survey_notes["Navigation"],
                    ],
                    "backgroundColor": ["rgba(54, 162, 235, 0.2)"],
                    "borderColor": ["rgba(54, 162, 235, 0.2)"],
                    "borderWidth": 1,
                },
                {
                    "label": self.object.selected_websites.first.name,
                    "data": [
                        website_notes["Quantity"],
                        website_notes["Quality"],
                        website_notes["Security"],
                        website_notes["Navigation"],
                    ],
                    "backgroundColor": ["rgba(255, 99, 132, 0.2)"],
                    "borderColor": ["rgba(255, 99, 132, 0.2)"],
                    "borderWidth": 1,
                },
            ],
        }

        return context
