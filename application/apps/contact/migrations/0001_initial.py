# Generated by Django 5.1 on 2024-12-04 18:32

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("email", models.EmailField(max_length=50)),
                ("subject", models.CharField(max_length=250)),
                ("message", models.TextField(max_length=10000)),
                ("created_at", models.DateTimeField(default=timezone.now)),
                ("read", models.BooleanField(default=False)),
            ],
        ),
    ]
