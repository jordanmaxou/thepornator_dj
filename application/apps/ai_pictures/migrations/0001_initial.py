# Generated by Django 5.1 on 2024-11-03 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("websites", "0004_migrate_websites_website"),
    ]

    operations = [
        migrations.CreateModel(
            name="AiOrNotAi",
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
                ("score", models.PositiveIntegerField(default=0)),
                ("ip", models.CharField(max_length=50)),
                ("date", models.DateTimeField()),
            ],
        ),
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
                ("name", models.CharField(max_length=50)),
                ("name_en", models.CharField(max_length=50, null=True)),
                ("name_fr", models.CharField(max_length=50, null=True)),
                ("slug", models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=50)),
                ("name_en", models.CharField(max_length=50, null=True)),
                ("name_fr", models.CharField(max_length=50, null=True)),
                ("slug", models.SlugField(blank=True)),
                ("icon", models.TextField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name="Note",
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
                ("funny", models.PositiveIntegerField(default=0)),
                ("sexy", models.PositiveIntegerField(default=0)),
                ("scary", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Content",
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
                ("title", models.CharField(max_length=200)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("title_fr", models.CharField(max_length=200, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("image", "Image"), ("video", "Video")], max_length=10
                    ),
                ),
                ("code", models.CharField(max_length=100)),
                ("publication_date", models.DateField()),
                ("categories", models.ManyToManyField(to="ai_pictures.category")),
                (
                    "source",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="websites.website",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ai_pictures.country",
                    ),
                ),
                (
                    "note",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ai_pictures.note",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(fields=["code"], name="ai_pictures_code_b46050_idx"),
                    models.Index(
                        fields=["source"], name="ai_pictures_source__bafd1f_idx"
                    ),
                    models.Index(
                        fields=["publication_date"],
                        name="ai_pictures_publica_42fc93_idx",
                    ),
                    models.Index(fields=["type"], name="ai_pictures_type_8b72ea_idx"),
                ],
            },
        ),
    ]
