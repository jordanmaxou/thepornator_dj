# Generated by Django 5.1 on 2024-11-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=100)),
                ("title_en", models.CharField(max_length=100, null=True)),
                ("title_fr", models.CharField(max_length=100, null=True)),
                ("content", models.TextField()),
                ("content_en", models.TextField(null=True)),
                ("content_fr", models.TextField(null=True)),
                ("publication_date", models.DateField()),
                ("thumb", models.FileField(upload_to="")),
                ("author", models.CharField(max_length=50)),
            ],
        ),
    ]
