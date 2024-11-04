# Generated by Django 5.1 on 2024-11-03 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
            ],
        ),
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
                ("clicks", models.PositiveIntegerField(default=0)),
                ("likes", models.PositiveIntegerField(default=0)),
                ("photos", models.PositiveIntegerField(default=0)),
                ("videos", models.PositiveIntegerField(default=0)),
                ("posts", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Website",
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
                ("slug", models.SlugField(blank=True, max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("slug", models.SlugField(blank=True, max_length=100)),
                ("pseudo", models.CharField(max_length=100)),
                ("photo", models.URLField()),
                ("description", models.TextField(max_length=500)),
                ("price", models.CharField(max_length=500)),
                ("categories", models.ManyToManyField(to="porn_models.category")),
                (
                    "counts",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="porn_models.count",
                    ),
                ),
                (
                    "website",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="porn_models.website",
                    ),
                ),
            ],
        ),
    ]