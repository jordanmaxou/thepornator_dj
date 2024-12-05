# Generated by Django 5.1 on 2024-11-03 16:29

from collections import defaultdict
from typing import Optional

from django.db import migrations
from apps.migration.utils import fetch_data_from_mysql
from os.path import join
from apps.ai_pictures.models import TypeOfContent


def create_categories_func(apps, _schema_editor):
    Category = apps.get_model("ai_pictures", "Category")

    category_objects = []
    categories = fetch_data_from_mysql("porn_aicategory")
    for category in categories:
        category_objects.append(
            Category(
                id=category.id,
                slug=category.slug,
                name=category.nameen,
                name_en=category.nameen,
                name_fr=category.namefr,
            )
        )
    Category.objects.bulk_create(category_objects)


def delete_categories_func(apps, _schema_editor):
    Category = apps.get_model("ai_pictures", "Category")
    categories = fetch_data_from_mysql("porn_aicategory")
    Category.objects.filter(id__in=[r.id for r in categories]).delete()


def create_countries_func(apps, _schema_editor):
    Country = apps.get_model("ai_pictures", "Country")
    country_objects = []
    countries = fetch_data_from_mysql("porn_country")
    for country in countries:
        country_objects.append(
            Country(
                id=country.id,
                slug=country.slug,
                name=country.nameen,
                name_en=country.nameen,
                name_fr=country.namefr,
                icon=country.svg_code,
            )
        )
    Country.objects.bulk_create(country_objects)


def delete_countries_func(apps, _schema_editor):
    Country = apps.get_model("ai_pictures", "Country")
    countries = fetch_data_from_mysql("porn_country")
    Country.objects.filter(id__in=[r.id for r in countries]).delete()


def get_extension_from_source(source: str, type: str) -> str:
    match source:
        case "pornjourney" | "donporn" | "candyai":
            return "png"
        case "pornmake" | "pornworks" | "pornworksai" | "createporn":
            if source in ["pornworks", "pornworksai"] and type == "video":
                return "webm"
            return "webp"
        case "deepmodeai":
            return "jpeg"
        case _:
            if type == "video":
                return "webm"
            return "jpg"


def get_image_url(source, slug) -> Optional[str]:
    match source:
        case "madeporn" if len(slug) == 23:
            return f"https://made.porn/600/is/{slug[9:11]}/{slug[7:9]}/{slug}.jpg"
        case "madeporn" if len(slug) == 22:
            return f"https://made.porn/600/is/{slug[8:10]}/{slug[6:8]}/{slug}.jpg"
        case "pornmake":
            return f"https://cdn.pornmake.ai/static/webp/{slug}.webp"
        case "pornxai":
            return f"https://cdn1.pornx.ai/{slug}"
        case "xpicturesio":
            return f"https://x-pictures-back-main.s3.us-east-2.amazonaws.com/media/generate-jobs/{slug}.jpeg"
        case "pornpen":
            return f"https://cdn.pornpen.ai/{slug}.jpg"
        case _:
            return None


def create_content_func(apps, _schema_editor):
    Website = apps.get_model("websites", "Website")
    Content = apps.get_model("ai_pictures", "Content")
    Note = apps.get_model("ai_pictures", "Note")
    Country = apps.get_model("ai_pictures", "Country")
    Category = apps.get_model("ai_pictures", "Category")
    content_category_relations = fetch_data_from_mysql("porn_aicontentcategory")
    content_category_map = defaultdict(list)
    for aicategory_id, aicontent_id in content_category_relations:
        content_category_map[aicontent_id].append(aicategory_id)
    content_category_map = dict(content_category_map)

    contents = fetch_data_from_mysql("porn_aicontent")
    for content in contents:
        note = Note.objects.create(
            funny=content.funny, sexy=content.sexy, scary=content.scary
        )
        content = Content.objects.create(
            id=content.id,
            external_url=get_image_url(content.source, content.code),
            title=content.titleEN,
            title_en=content.titleEN,
            title_fr=content.titleFR,
            type=content.type,
            slug=content.code,
            publication_date=content.publicationdate,
            note=note,
            source=Website.objects.filter(
                slug=content.source if content.source != "pornworks" else "pornworksai"
            ).first(),
            image=join(
                "img/aicontent" if content.type == "image" else "video/aicontent",
                f"{content.code}.{get_extension_from_source(content.source, content.type)}",
            ),
            country=Country.objects.get(id=content.country_id)
            if content.country_id
            else None,
            status=1,
        )
        for aicategory_id in content_category_map.get(content.id, []):
            content.categories.add(Category.objects.get(id=aicategory_id))


def delete_content_func(apps, _schema_editor):
    Content = apps.get_model("ai_pictures", "Content")
    contents = fetch_data_from_mysql("porn_aicontent")
    content_ids = [r.id for r in contents]
    Content.objects.filter(id__in=content_ids).delete()
    ContentCategory = Content.categories.through
    ContentCategory.objects.filter(content_id__in=content_ids).delete()


def update_category_with_main_contents(apps, _schema_editor):
    Content = apps.get_model("ai_pictures", "Content")
    Category = apps.get_model("ai_pictures", "Category")
    for category in Category.objects.all():
        main_image_content = Content.objects.filter(
            categories=category, type=TypeOfContent.IMAGE
        ).first()
        main_video_content = Content.objects.filter(
            categories=category, type=TypeOfContent.VIDEO
        ).first()
        category.main_image_content_id = (
            main_image_content.id if main_image_content else None
        )
        category.main_video_content_id = (
            main_video_content.id if main_video_content else None
        )
        category.save()


def update_category_main_contents_to_none(apps, _schema_editor):
    Category = apps.get_model("ai_pictures", "Category")
    for category in Category.objects.all():
        category.main_image_content = None
        category.main_video_content = None
        category.save()


def update_country_with_main_image_content(apps, _schema_editor):
    Content = apps.get_model("ai_pictures", "Content")
    Country = apps.get_model("ai_pictures", "Country")
    for country in Country.objects.all():
        main_image_content = Content.objects.filter(
            country_id=country.id, type=TypeOfContent.IMAGE
        ).first()
        if main_image_content:
            country.main_content_id = main_image_content.id
            country.save()


def update_country_main_image_content_to_none(apps, _schema_editor):
    Country = apps.get_model("ai_pictures", "Country")
    for country in Country.objects.all():
        country.main_content = None
        country.save()


def create_tags_func(apps, _schema_editor):
    Content = apps.get_model("ai_pictures", "Content")
    Tag = apps.get_model("ai_pictures", "Tag")
    tags = fetch_data_from_mysql("porn_ngram")
    tags_contents_relations = fetch_data_from_mysql("porn_ngram_aicontent")
    tag_contents_map = defaultdict(list)
    for tag_id, aicontent_id in tags_contents_relations:
        tag_contents_map[tag_id].append(aicontent_id)
    tag_contents_map = dict(tag_contents_map)
    for tag in tags:
        current_tag = Tag.objects.create(
            id=tag.id, name=tag.label, slug=tag.slug, lang=tag.lang
        )
        for content_id in tag_contents_map[tag.id]:
            current_tag.contents.add(Content.objects.get(id=content_id))


def remove_tags_func(apps, _schema_editor):
    Tag = apps.get_model("ai_pictures", "Tag")
    tags = fetch_data_from_mysql("porn_ngram")
    tag_ids = [r.id for r in tags]
    Tag.objects.filter(id__in=tag_ids).delete()
    TagContent = Tag.contents.through
    TagContent.objects.filter(tag_id__in=tag_ids).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("ai_pictures", "0002_initial"),
        ("websites", "0004_migrate_websites_website"),
    ]

    operations = [
        migrations.RunPython(
            create_categories_func, delete_categories_func, atomic=True
        ),
        migrations.RunPython(create_countries_func, delete_countries_func, atomic=True),
        migrations.RunPython(create_content_func, delete_content_func, atomic=True),
        migrations.RunPython(create_tags_func, remove_tags_func, atomic=True),
        migrations.RunPython(
            update_category_with_main_contents,
            update_category_main_contents_to_none,
            atomic=True,
        ),
        migrations.RunPython(
            update_country_with_main_image_content,
            update_country_main_image_content_to_none,
            atomic=True,
        ),
    ]
