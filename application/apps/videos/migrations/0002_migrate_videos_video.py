# Generated by Django 5.1 on 2024-11-03 20:03

from datetime import timedelta
from os.path import join

from django.db import migrations
from apps.migration.utils import fetch_data_from_mysql


def create_categories_func(apps, _schema_editor):
    Category = apps.get_model("videos", "Category")

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
    Category = apps.get_model("videos", "Category")
    categories = fetch_data_from_mysql("porn_videocategory")
    Category.objects.filter(id__in=[r.id for r in categories]).delete()


def create_channel_func(apps, _schema_editor):
    Channel = apps.get_model("videos", "Channel")

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
                icon=join("img/logosites", channel.logo),
                link=channel.link,
            )
        )
    Channel.objects.bulk_create(channels_objects)


def delete_channel_func(apps, _schema_editor):
    Channel = apps.get_model("videos", "Channel")
    channels = fetch_data_from_mysql("porn_videochannel")
    Channel.objects.filter(id__in=[r.id for r in channels]).delete()


def create_video_func(apps, _schema_editor):
    Count = apps.get_model("videos", "Count")
    Video = apps.get_model("videos", "Video")

    videos = fetch_data_from_mysql("porn_videodetail")
    for video in videos:
        count = Count.objects.create(
            up=video.up,
            down=video.down,
            clicks=video.click,
        )
        Video.objects.create(
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
            local_main_thumb=join("img/video", f"{video.slug}.jpg"),
            publication_date=video.publicationdate,
            duration=timedelta(seconds=video.duration) if video.duration else None,
            channel_id=video.channel_id,
            counts=count,
            enabled=True if video.status == 1 else False,
        )


def delete_video_func(apps, _schema_editor):
    Video = apps.get_model("videos", "Video")
    videos = fetch_data_from_mysql("porn_videodetail")
    video_ids = [r.id for r in videos]
    Video.objects.filter(id__in=video_ids).delete()


def create_video_category_func(apps, _schema_editor):
    Video = apps.get_model("videos", "Video")
    ContentCategory = Video.categories.through
    video_categories = fetch_data_from_mysql("porn_videodetailcategory")
    video_category_objs = []
    for video_category in video_categories:
        video_category_objs.append(
            ContentCategory(
                video_id=video_category.videodetail_id,
                category_id=video_category.videocategory_id,
            )
        )
    ContentCategory.objects.bulk_create(video_category_objs)


def delete_video_category_func(apps, _schema_editor):
    Video = apps.get_model("videos", "Video")
    ContentCategory = Video.categories.through
    video_categories = fetch_data_from_mysql("porn_videodetailcategory")
    ContentCategory.objects.filter(
        video_id__in=[
            video_categories.videodetail_id for video_categories in video_categories
        ]
    ).delete()


def update_category_with_main_content(apps, _schema_editor):
    Video = apps.get_model("videos", "Video")
    Category = apps.get_model("videos", "Category")
    for category in Category.objects.all():
        main_content = Video.objects.filter(categories=category).first()
        category.main_content_id = main_content.id if main_content else None
        category.save()


def update_category_main_content_to_none(apps, _schema_editor):
    Category = apps.get_model("videos", "Category")
    for category in Category.objects.all():
        category.main_content = None
        category.save()


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_categories_func, delete_categories_func, atomic=True
        ),
        migrations.RunPython(create_channel_func, delete_channel_func, atomic=True),
        migrations.RunPython(create_video_func, delete_video_func, atomic=True),
        migrations.RunPython(
            create_video_category_func, delete_video_category_func, atomic=True
        ),
        migrations.RunPython(
            update_category_with_main_content,
            update_category_main_content_to_none,
            atomic=True,
        ),
    ]
