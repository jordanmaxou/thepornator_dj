# Generated by Django 5.1 on 2024-11-22 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.SmallIntegerField()),
                ("sentence", models.CharField(max_length=150)),
                ("sentence_en", models.CharField(max_length=150, null=True)),
                ("sentence_fr", models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Survey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_daily_fingerprint",
                    models.CharField(max_length=255, unique=True),
                ),
                ("creation_date", models.DateField(auto_now_add=True)),
                ("is_valid", models.BooleanField(default=False)),
                ("duration", models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name="Theme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_en", models.CharField(max_length=100, null=True)),
                ("name_fr", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="QuestionSurvey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("note", models.PositiveIntegerField(default=0)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="surveys.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionWebsite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("note_init", models.PositiveIntegerField(default=0)),
                ("note_update", models.PositiveIntegerField(default=0)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="surveys.question",
                    ),
                ),
            ],
        ),
    ]
