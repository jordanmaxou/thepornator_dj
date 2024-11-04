# Generated by Django 5.1 on 2024-11-02 19:25

from django.db import migrations
from apps.migration.utils import fetch_data_from_mysql


def create_categories_func(apps, _schema_editor):
    Category = apps.get_model("websites", "Category")

    category_objects = []
    categories = fetch_data_from_mysql("porn_category")
    for category in categories:
        category_objects.append(
            Category(
                id=category.id,
                slug=category.slug,
                name=category.labelEN,
                name_en=category.labelEN,
                name_fr=category.labelFR,
                description=category.descriptionEN,
                description_en=category.descriptionEN,
                description_fr=category.descriptionFR,
                position=category.position,
                icon=category.icon,
            )
        )
    Category.objects.bulk_create(category_objects)


def delete_categories_func(apps, schema_editor):
    Category = apps.get_model("websites", "Category")
    categories = fetch_data_from_mysql("porn_category")
    Category.objects.filter(id__in=[r.id for r in categories]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("websites", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_categories_func, delete_categories_func),
    ]