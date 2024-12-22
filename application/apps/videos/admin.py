import chardet
from datetime import timedelta

from django.contrib import admin
from django.urls import path
from django import forms
from django.db import transaction
from django.shortcuts import redirect, render

from apps.videos.models import Video, Channel, Category, Count


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("slug", "title_fr", "title_en", "channel", "duration")
    exclude = ("title", "description")
    readonly_fields = ("counts",)
    list_filter = ("channel__slug",)

    def get_urls(self):
        urls = super().get_urls()
        return [
            path(
                "upload-videos-from-csv/",
                self.upload_csv,
                name="upload-videos-from-csv",
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
                    for i, row in enumerate(data):
                        (
                            title_en,
                            title_fr,
                            description_en,
                            description_fr,
                            link,
                            main_thumb,
                            duration,
                            publication_date,
                            channel,
                            categories,
                        ) = row.split(";")
                        video = Video.objects.create(
                            title_en=title_en,
                            title_fr=title_fr,
                            description_en=description_en,
                            description_fr=description_fr,
                            link=link,
                            main_thumb=main_thumb,
                            duration=timedelta(seconds=int(duration))
                            if duration
                            else None,
                            publication_date=publication_date,
                            channel=Channel.objects.get(slug=channel.strip()),
                            counts=Count.objects.create(),
                        )
                        for category in categories.split(","):
                            video.categories.add(
                                Category.objects.get(slug=category.strip())
                            )
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
        payload = {"form": form, "subtitle": "Upload CSV for videos video"}
        context = self.admin_site.each_context(request)
        return render(
            request, "admin/videos/video/csv_form.html", {**context, **payload}
        )


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Count)
class CountAdmin(admin.ModelAdmin):
    pass
