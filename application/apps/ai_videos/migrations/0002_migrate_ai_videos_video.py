# Generated by Django 5.1 on 2024-11-03 20:03

from collections import defaultdict
from datetime import timedelta

from django.db import migrations
from apps.migration.utils import fetch_data_from_mysql


def create_categories_func(apps, _schema_editor):
    Category = apps.get_model("ai_videos", "Category")

    category_objects = []
    categories = fetch_data_from_mysql("porn_videocategory")
    for category in categories:
        category_objects.append(
            Category(
                id=category.id,
                slug=category.slug,
                name=category.nameEN,
                name_en=category.nameEN,
                name_fr=category.nameFR,
                description=category.descriptionEN,
                description_en=category.descriptionEN,
                description_fr=category.descriptionFR,
            )
        )
    Category.objects.bulk_create(category_objects)


def delete_categories_func(apps, _schema_editor):
    Category = apps.get_model("ai_videos", "Category")
    categories = fetch_data_from_mysql("porn_videocategory")
    Category.objects.filter(id__in=[r.id for r in categories]).delete()


def create_channel_func(apps, _schema_editor):
    Channel = apps.get_model("ai_videos", "Channel")

    channels_objects = []
    channels = fetch_data_from_mysql("porn_videochannel")
    for channel in channels:
        channels_objects.append(
            Channel(
                id=channel.id,
                slug=channel.slug,
                name=channel.label,
                description=channel.descriptionEN,
                description_en=channel.descriptionEN,
                description_fr=channel.descriptionFR,
                logo=channel.logo,
                link=channel.link,
            )
        )
    Channel.objects.bulk_create(channels_objects)


def delete_channel_func(apps, _schema_editor):
    Channel = apps.get_model("ai_videos", "Channel")
    channels = fetch_data_from_mysql("porn_videochannel")
    Channel.objects.filter(id__in=[r.id for r in channels]).delete()


def create_video_func(apps, _schema_editor):
    Category = apps.get_model("ai_videos", "Category")
    Count = apps.get_model("ai_videos", "Count")
    Channel = apps.get_model("ai_videos", "Channel")
    Video = apps.get_model("ai_videos", "Video")

    video_category_relations = fetch_data_from_mysql("porn_videodetailcategory")
    video_category_map = defaultdict(list)
    for videodetail_id, videocategory_id in video_category_relations:
        video_category_map[videodetail_id].append(videocategory_id)
    video_category_map = dict(video_category_map)

    videos = fetch_data_from_mysql("porn_videodetail")
    for video in videos:
        count = Count.objects.create(
            up=video.up,
            down=video.down,
            clicks=video.click,
        )
        video_obj = Video.objects.create(
            id=video.id,
            slug=video.slug,
            title=video.titleEN,
            title_en=video.titleEN,
            title_fr=video.titleFR,
            description=video.descriptionEN,
            description_en=video.descriptionEN,
            description_fr=video.descriptionFR,
            link=video.link,
            main_thumb=video.mainthumb,
            publication_date=video.publicationdate,
            duration=timedelta(seconds=video.duration) if video.duration else None,
            channel=Channel.objects.get(id=video.channel_id),
            counts=count,
            enabled=True if video.status == 1 else False,
        )
        for category_id in video_category_map.get(video.id, []):
            video_obj.categories.add(Category.objects.get(id=category_id))


def delete_video_func(apps, _schema_editor):
    Video = apps.get_model("ai_videos", "Video")
    videos = fetch_data_from_mysql("porn_videodetail")
    video_ids = [r.id for r in videos]
    Video.objects.filter(id__in=video_ids).delete()
    ContentCategory = Video.categories.through
    ContentCategory.objects.filter(video_id__in=video_ids).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("ai_videos", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_categories_func, delete_categories_func),
        migrations.RunPython(create_channel_func, delete_channel_func),
        migrations.RunPython(create_video_func, delete_video_func),
    ]
