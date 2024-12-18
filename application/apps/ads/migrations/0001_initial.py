# Generated by Django 5.1 on 2024-11-27 19:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banner",
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
                ("weight", models.PositiveSmallIntegerField(default=1)),
                (
                    "languages",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[("fr", "Fr"), ("en", "En")], max_length=2
                        ),
                        size=None,
                    ),
                ),
                (
                    "device",
                    models.CharField(
                        choices=[("mobile", "Mobile"), ("desktop", "Desktop")],
                        max_length=10,
                    ),
                ),
                (
                    "zones",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("top", "Top"),
                                ("bottom", "Bottom"),
                                ("middle", "Middle"),
                            ],
                            max_length=10,
                        ),
                        size=None,
                    ),
                ),
                ("target_url", models.URLField(max_length=250)),
                ("image", models.ImageField(upload_to="img/banners")),
                ("enabled", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="TopLink",
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
                ("label", models.CharField(max_length=100)),
                ("link", models.URLField(max_length=250)),
                (
                    "lang",
                    models.CharField(
                        choices=[("fr", "Fr"), ("en", "En")], max_length=2
                    ),
                ),
                ("enabled", models.BooleanField(default=True)),
                ("position", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
