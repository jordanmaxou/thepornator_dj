from datetime import date
import chardet

from django.contrib import admin
from django import forms
from django.urls import path
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.db import transaction

from apps.ai_pictures.models import Content, TypeOfStatus, Category, Country, Note
from apps.websites.models import Website


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
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
    ordering = ("-publication_date", "status", "title")
    readonly_fields = ("note", "slug")
    exclude = ("title",)
    list_filter = ("type", "publication_date")

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
