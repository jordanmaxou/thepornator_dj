# Generated by Django 5.1 on 2024-11-22 17:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0004_podium_survey_selected_websites"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="survey",
            name="selected_website",
        ),
    ]
