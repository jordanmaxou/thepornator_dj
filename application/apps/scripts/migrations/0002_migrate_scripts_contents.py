# Generated by Django 5.1 on 2024-11-04 08:13

from os.path import join

from django.db import migrations
from apps.migration.utils import fetch_data_from_mysql


def create_content_func(apps, _schema_editor):
    Content = apps.get_model("scripts", "Content")
    contents = fetch_data_from_mysql("porn_scriptcontent")
    content_objects = []
    for content in contents:
        content_objects.append(
            Content(
                id=content.id,
                slug=content.slug,
                title=content.title,
                studio=content.studio,
                link=content.link,
                thumb=join("img/script", content.thumb),
                text=content.text,
                publication_date=content.publicationdate,
                lang=content.lang,
            )
        )
    Content.objects.bulk_create(content_objects)


def delete_content_func(apps, _schema_editor):
    Content = apps.get_model("scripts", "Content")
    contents = fetch_data_from_mysql("porn_scriptcontent")
    Content.objects.filter(id__in=[r.id for r in contents]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("scripts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_content_func, delete_content_func),
    ]
