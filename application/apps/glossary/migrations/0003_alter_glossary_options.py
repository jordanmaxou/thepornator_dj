# Generated by Django 5.1 on 2024-11-29 09:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("glossary", "0002_migrate_glossary_glossary"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="glossary",
            options={"verbose_name_plural": "glossary"},
        ),
    ]