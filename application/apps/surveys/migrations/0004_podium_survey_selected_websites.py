# Generated by Django 5.1 on 2024-11-22 16:17

import django.db.models.deletion
from django.db import migrations, models


def update_selected_websites(apps, _schema_editor):
    Survey = apps.get_model("surveys", "Survey")
    Podium = apps.get_model("surveys", "Podium")
    for survey in Survey.objects.all():
        if survey.selected_website:
            podium = Podium.objects.create(
                first=survey.selected_website, second=None, third=None
            )
            survey.selected_websites = podium
            survey.save()


def delete_podiums(apps, _schema_editor):
    Podium = apps.get_model("surveys", "Podium")
    Podium.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0003_migrate_surveys_survey"),
        ("websites", "0004_migrate_websites_website"),
    ]

    operations = [
        migrations.CreateModel(
            name="Podium",
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
                    "first",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="websites.website",
                    ),
                ),
                (
                    "second",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="websites.website",
                    ),
                ),
                (
                    "third",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="websites.website",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="survey",
            name="selected_websites",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="surveys.podium",
            ),
        ),
        migrations.RunPython(
            update_selected_websites, migrations.RunPython.noop, atomic=True
        ),
    ]
