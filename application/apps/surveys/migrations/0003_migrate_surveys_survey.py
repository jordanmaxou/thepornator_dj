# Generated by Django 5.1 on 2024-11-04 07:08

from django.db import migrations
from django.db.models import Count
from apps.migration.utils import fetch_data_from_mysql
from datetime import timedelta


def create_theme_func(apps, _schema_editor):
    Theme = apps.get_model("surveys", "Theme")
    theme_objects = []
    themes = fetch_data_from_mysql("porn_theme")
    for theme in themes:
        theme_objects.append(
            Theme(
                id=theme.id,
                name=theme.labelEN,
                name_en=theme.labelEN,
                name_fr=theme.labelFR,
            )
        )
    Theme.objects.bulk_create(theme_objects)


def delete_theme_func(apps, _schema_editor):
    Theme = apps.get_model("surveys", "Theme")
    themes = fetch_data_from_mysql("porn_theme")
    Theme.objects.filter(id__in=[r.id for r in themes]).delete()


def create_question_func(apps, _schema_editor):
    Question = apps.get_model("surveys", "Question")
    question_objects = []
    questions = fetch_data_from_mysql("porn_question")
    for question in questions:
        question_objects.append(
            Question(
                id=question.id,
                sentence=question.labelEN,
                sentence_en=question.labelEN,
                sentence_fr=question.labelFR,
                theme_id=question.theme_id,
                position=question.id,
            )
        )
    Question.objects.bulk_create(question_objects)


def delete_question_func(apps, _schema_editor):
    Question = apps.get_model("surveys", "Question")
    questions = fetch_data_from_mysql("porn_question")
    Question.objects.filter(id__in=[r.id for r in questions]).delete()


def create_survey_func(apps, _schema_editor):
    Survey = apps.get_model("surveys", "Survey")
    survey_objects = []
    surveys = fetch_data_from_mysql("porn_survey")
    for survey in surveys:
        survey_objects.append(
            Survey(
                id=survey.id,
                user_daily_fingerprint=survey.hash,
                creation_date=survey.updatedate,
                selected_website_id=survey.site_id,
                is_valid=bool(survey.is_validated)
                if survey.is_validated is not None
                else None,
                duration=timedelta(seconds=survey.duration),
            )
        )
    Survey.objects.bulk_create(
        survey_objects, ignore_conflicts=True, unique_fields=["user_daily_fingerprint"]
    )


def delete_survey_func(apps, _schema_editor):
    Survey = apps.get_model("surveys", "Survey")
    surveys = fetch_data_from_mysql("porn_survey")
    Survey.objects.filter(id__in=[r.id for r in surveys]).delete()


def create_question_survey_func(apps, _schema_editor):
    Survey = apps.get_model("surveys", "Survey")
    QuestionSurvey = apps.get_model("surveys", "QuestionSurvey")
    question_survey_objs = []
    question_surveys = fetch_data_from_mysql("porn_questionsurvey")
    surveys = Survey.objects.values_list("id", flat=True)
    for question_survey in question_surveys:
        if question_survey.survey_id in surveys:
            question_survey_objs.append(
                QuestionSurvey(
                    question_id=question_survey.question_id,
                    survey_id=question_survey.survey_id,
                    note=question_survey.note,
                )
            )
    QuestionSurvey.objects.bulk_create(question_survey_objs)


def delete_question_survey_func(apps, _schema_editor):
    QuestionSurvey = apps.get_model("surveys", "QuestionSurvey")
    questions = fetch_data_from_mysql("porn_question")
    QuestionSurvey.objects.filter(question_id__in=questions).delete()


def create_question_website_func(apps, _schema_editor):
    QuestionWebsite = apps.get_model("surveys", "QuestionWebsite")
    question_websites = fetch_data_from_mysql("porn_questionsite")
    question_website_objs = []
    for question_website in question_websites:
        if question_website.site_id != 0:  # I don't understand, no website with id = 0
            question_website_objs.append(
                QuestionWebsite(
                    question_id=question_website.question_id,
                    website_id=question_website.site_id,
                    note_init=question_website.note_init,
                    note_update=question_website.note_update,
                )
            )
    QuestionWebsite.objects.bulk_create(question_website_objs)


def delete_question_website_func(apps, _schema_editor):
    QuestionWebsite = apps.get_model("surveys", "QuestionWebsite")
    questions = fetch_data_from_mysql("porn_question")
    QuestionWebsite.objects.filter(question_id__in=questions).delete()


def remove_duplicated_rows(apps, _schema_editor):
    Survey = apps.get_model("surveys", "survey")
    for s in (
        Survey.objects.values("user_daily_fingerprint")
        .annotate(nb=Count("id"))
        .filter(nb__gt=1)
    ):
        _ = (
            Survey.objects.filter(user_daily_fingerprint=s["user_daily_fingerprint"])
            .first()
            .delete()
        )


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0002_initial"),
        ("websites", "0004_migrate_websites_website"),
    ]

    operations = [
        migrations.RunPython(create_theme_func, delete_theme_func, atomic=True),
        migrations.RunPython(create_question_func, delete_question_func, atomic=True),
        migrations.RunPython(create_survey_func, delete_survey_func, atomic=True),
        migrations.RunPython(
            create_question_survey_func, delete_question_survey_func, atomic=True
        ),
        migrations.RunPython(
            create_question_website_func, delete_question_website_func, atomic=True
        ),
        migrations.RunPython(
            remove_duplicated_rows, migrations.RunPython.noop, atomic=True
        ),
    ]
