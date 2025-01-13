# Generated by Django 5.1 on 2025-01-13 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("websites", "0006_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="website",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="websites.category",
            ),
        ),
        migrations.AlterField(
            model_name="website",
            name="deal",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="websites.deal",
            ),
        ),
    ]
