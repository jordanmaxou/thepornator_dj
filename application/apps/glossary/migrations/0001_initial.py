# Generated by Django 5.1 on 2024-11-03 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Count",
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
                ("up", models.PositiveIntegerField(default=0)),
                ("down", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Glossary",
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
                ("slug", models.SlugField(blank=True)),
                ("name", models.CharField(max_length=50)),
                ("name_en", models.CharField(max_length=50, null=True)),
                ("name_fr", models.CharField(max_length=50, null=True)),
                ("type", models.CharField(max_length=50)),
                ("meaning", models.TextField(max_length=100, null=True)),
                ("definition", models.TextField(max_length=1200)),
                ("definition_en", models.TextField(max_length=1200, null=True)),
                ("definition_fr", models.TextField(max_length=1200, null=True)),
                ("picture", models.FileField(upload_to="")),
                ("publication_date", models.DateField()),
                ("lang", models.CharField(max_length=5, null=True)),
                (
                    "count",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="glossary.count"
                    ),
                ),
            ],
        ),
    ]
