# Generated by Django 5.1 on 2024-11-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trends", "0002_migrate_statistics_trending_searches"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trendingsearches",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
    ]
