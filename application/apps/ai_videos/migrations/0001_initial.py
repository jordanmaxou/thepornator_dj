# Generated by Django 5.1 on 2024-11-03 21:13

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
                ("slug", models.SlugField(blank=True, max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("name_en", models.CharField(max_length=100, null=True)),
                ("name_fr", models.CharField(max_length=100, null=True)),
                ("description", models.TextField()),
                ("description_en", models.TextField(null=True)),
                ("description_fr", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Channel",
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
                ("logo", models.FileField(upload_to="")),
                ("link", models.URLField()),
                ("description", models.TextField(max_length=500)),
                ("description_en", models.TextField(max_length=500, null=True)),
                ("description_fr", models.TextField(max_length=500, null=True)),
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
                ("up", models.PositiveIntegerField(default=0)),
                ("down", models.PositiveIntegerField(default=0)),
                ("clicks", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Video",
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
                ("slug", models.SlugField(blank=True, max_length=250)),
                ("title", models.CharField(max_length=250)),
                ("title_en", models.CharField(max_length=250, null=True)),
                ("title_fr", models.CharField(max_length=250, null=True)),
                ("description", models.TextField(max_length=800)),
                ("description_en", models.TextField(max_length=800, null=True)),
                ("description_fr", models.TextField(max_length=800, null=True)),
                ("link", models.URLField(max_length=250)),
                ("main_thumb", models.URLField()),
                ("publication_date", models.DateField()),
                ("duration", models.DurationField(null=True)),
                ("enabled", models.BooleanField(default=True)),
                ("categories", models.ManyToManyField(to="ai_videos.category")),
                (
                    "channel",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ai_videos.channel",
                    ),
                ),
                (
                    "counts",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ai_videos.count",
                    ),
                ),
            ],
        ),
    ]
