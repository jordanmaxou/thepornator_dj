# Generated by Django 5.1 on 2024-11-26 14:02

from datetime import datetime
import requests
import json
from os.path import join
from django.db import migrations


def create_banner_entries(apps, _schema_editor):
    Banner = apps.get_model("ads", "Banner")
    response = requests.get(
        f"https://thepornator.com/assets/json/banners.json?t={int(datetime.now().timestamp())}"
    )
    if response.ok:
        banner_objs = []
        banners = json.loads(response.content)
        for banner_data in banners:
            banner_objs.append(
                Banner(
                    weight=banner_data["weight"],
                    languages=banner_data["lang"].split("|"),
                    device=banner_data["device"],
                    target_url=banner_data["targetUrl"],
                    zones=banner_data["zone"].split("|"),
                    image=join("img/banners", banner_data["imagename"]),
                )
            )
        Banner.objects.bulk_create(banner_objs)


def delete_banner_entries(apps, _schema_editor):
    Banner = apps.get_model("ads", "Banner")
    Banner.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_banner_entries, delete_banner_entries)]
