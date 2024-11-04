# Generated by Django 5.1 on 2024-11-03 21:40

from django.db import migrations
from apps.migration.utils import fetch_data_from_mysql


def create_blog_func(apps, _schema_editor):
    Blog = apps.get_model("blog", "Blog")
    blog_objects = []
    blogs = fetch_data_from_mysql("porn_blog")
    for blog in blogs:
        blog_objects.append(
            Blog(
                id=blog.id,
                slug=blog.slug,
                title=blog.titleEN,
                title_en=blog.titleEN,
                title_fr=blog.titleFR,
                content=blog.contentEN,
                content_en=blog.contentEN,
                content_fr=blog.contentFR,
                publication_date=blog.publicationdate,
                thumb=blog.thumb,
                author=blog.author,
            )
        )
    Blog.objects.bulk_create(blog_objects)


def delete_blog_func(apps, _schema_editor):
    Blog = apps.get_model("blog", "Blog")
    blogs = fetch_data_from_mysql("porn_blog")
    Blog.objects.filter(id__in=[r.id for r in blogs]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_blog_func, delete_blog_func),
    ]