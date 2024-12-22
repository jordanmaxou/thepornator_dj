from datetime import date
import chardet

from django.db.models import ManyToManyField
from django.contrib import admin
from django import forms
from django.urls import path
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.db import transaction

from apps.ai_pictures.models import (
    Content,
    TypeOfStatus,
    TypeOfContent,
    Category,
    Country,
    Note,
    AiOrNotAiScore,
    AiOrNotAiImage,
)
from apps.ai_pictures.utils import extract_code_from_url
from apps.websites.models import Website


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class PublishedStatusFilter(admin.SimpleListFilter):
    title = "Published status"
    parameter_name = "published_status"

    def lookups(self, request, model_admin):
        return [
            ("published", "published"),
            ("unpublished", "unpublished"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "published":
            return queryset.filter(
                status=TypeOfStatus.OK, publication_date__lte=date.today()
            )
        if self.value() == "unpublished":
            return queryset.filter(
                status=TypeOfStatus.OK, publication_date__gt=date.today()
            )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ManyToManyField: {
            "widget": forms.CheckboxSelectMultiple,
        },
    }

    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["categories"].queryset = form.base_fields[
            "categories"
        ].queryset.order_by("slug")
        return form

    search_fields = ("slug", "title_fr", "title_en")
    list_display = (
        "title",
        "type",
        "slug",
        "created_at",
        "display_publication_date",
        "display_status",
        "created_at",
    )
    ordering = ("-created_at", "-publication_date", "status", "title")
    readonly_fields = ("note", "slug", "preview_image")
    exclude = ("title",)
    fields = (
        "slug",
        "title_en",
        "title_fr",
        "type",
        "created_at",
        "publication_date",
        "status",
        "source",
        "country",
        "categories",
        "image",
        "preview_image",
        "external_url",
        "note",
    )
    list_filter = ("type", PublishedStatusFilter)

    def preview_image(self, obj):
        if obj.image:
            if obj.type == TypeOfContent.IMAGE:
                return format_html(
                    '<img src="{}" style="max-height:512px"/>'.format(obj.image.url)
                )
            else:
                return format_html(
                    '<video src="{}" style="max-height:512px"/>'.format(obj.image.url)
                )

    def get_urls(self):
        urls = super().get_urls()
        return [
            path(
                "upload-aipictures-from-csv/",
                self.upload_csv,
                name="upload-aipictures-from-csv",
            ),
            *urls,
        ]

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            raw_data = csv_file.read()
            encoding = chardet.detect(raw_data).get("encoding", "utf-8")
            data = raw_data.decode(encoding).splitlines()

            try:
                with transaction.atomic():
                    sources_map = {}
                    countries_map = {}
                    categories_map = {}
                    for i, row in enumerate(data):
                        (
                            type,
                            title_en,
                            title_fr,
                            url,
                            source,
                            country,
                            categories,
                            publication_date,
                        ) = row.split(";")
                        publication_date = date.fromisoformat(publication_date)
                        sources_map[source] = sources_map.get(
                            source, Website.objects.get(slug=source)
                        )
                        countries_map[country] = countries_map.get(
                            country, Country.objects.get(slug=country)
                        )
                        content = Content.objects.create(
                            slug=extract_code_from_url(url),
                            type=type,
                            title_en=title_en,
                            title_fr=title_fr,
                            external_url=url,
                            source=sources_map[source],
                            country=countries_map[country],
                            publication_date=publication_date,
                            note=Note.objects.create(),
                        )
                        for category in categories.split(","):
                            categories_map[category] = categories_map.get(
                                category, Category.objects.get(slug=category)
                            )
                            content.categories.add(categories_map[category])
            except Exception as e:
                self.message_user(
                    request,
                    f"A problem occurs during csv importation at line {i + 1}\n{str(e)}",
                    level=40,
                )
                return redirect("..")
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form, "subtitle": "Upload CSV for ai_pictures contents"}
        context = self.admin_site.each_context(request)
        return render(
            request, "admin/ai_pictures/content/csv_form.html", {**context, **payload}
        )

    def display_publication_date(self, obj):
        red, green = "#3C1518", "#69995D"
        if obj.publication_date > date.today():
            color = red
        else:
            color = green
        return format_html(
            f"<span style='background-color: {color};'>{obj.publication_date}</span>"
        )

    def display_status(self, obj):
        red, orange, green = "#3C1518", "#FFBE86", "#69995D"
        if obj.status is not None:
            if obj.status == TypeOfStatus.OK:
                color = green
            elif obj.status == TypeOfStatus.NOT_FOUND:
                color = red
            else:
                color = orange
            return format_html(
                f"<span style='background-color: {color}'>{obj.get_status_display().upper()}</span>"
            )

    display_publication_date.admin_order_field = "publication_date"
    display_status.admin_order_field = "status"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("slug", "name_en", "name_fr")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("slug", "name_en", "name_fr")


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "funny", "sexy", "scary")


@admin.register(AiOrNotAiScore)
class AiOrNotAiScoreAdmin(admin.ModelAdmin):
    ordering = ("-date",)
    list_display = ("ip", "score", "date")


@admin.register(AiOrNotAiImage)
class AiOrNotAiImageAdmin(admin.ModelAdmin):
    list_display = ("id", "is_real", "enabled", "display_icon")

    def display_icon(self, obj):
        if obj.picture:
            return format_html(
                '<img src="{}" style="max-height:45px"/>'.format(obj.picture.url)
            )
