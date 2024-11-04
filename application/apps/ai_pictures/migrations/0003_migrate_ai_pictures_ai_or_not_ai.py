# Generated by Django 5.1 on 2024-11-03 18:21

from django.db import migrations
from apps.migration.utils import fetch_data_from_mysql
from datetime import timezone


def create_ai_or_not_ai_func(apps, _schema_editor):
    AiOrNotAi = apps.get_model("ai_pictures", "AiOrNotAi")

    aiornotai_objects = []
    aiornotais = fetch_data_from_mysql("porn_aiornotai")
    for aiornotai in aiornotais:
        aiornotai_objects.append(
            AiOrNotAi(
                id=aiornotai.id,
                score=aiornotai.score,
                ip=aiornotai.ip,
                date=aiornotai.date.replace(tzinfo=timezone.utc),
            )
        )
    AiOrNotAi.objects.bulk_create(aiornotai_objects)


def delete_ai_or_not_ai_func(apps, _schema_editor):
    AiOrNotAi = apps.get_model("ai_pictures", "AiOrNotAi")
    aiornotais = fetch_data_from_mysql("porn_aiornotai")
    AiOrNotAi.objects.filter(id__in=[r.id for r in aiornotais]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("ai_pictures", "0002_migrate_ai_pictures_contents"),
    ]

    operations = [
        migrations.RunPython(create_ai_or_not_ai_func, delete_ai_or_not_ai_func),
    ]
