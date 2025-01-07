import chardet

from django.contrib import admin
from django import forms
from django.urls import path
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.db import transaction, models

from apps.porn_models.models import Profile, Category, Website, Count, TypeOfStatus
from apps.porn_models.utils import extract_categories


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pseudo", "slug", "website", "display_status")
    list_filter = ("status", "website__slug")
    readonly_fields = ("counts",)

    formfield_overrides = {
        models.ManyToManyField: {
            "widget": forms.CheckboxSelectMultiple,
        },
    }

    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["categories"].queryset = form.base_fields[
            "categories"
        ].queryset.order_by("slug")
        return form

    def get_urls(self):
        urls = super().get_urls()
        return [
            path(
                "upload-models-from-csv/",
                self.upload_csv,
                name="upload-models-from-csv",
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
                    flatten_terms_map = Category.objects.flatten_terms()
                    flatten_terms = flatten_terms_map.keys()
                    sources_map = {}
                    categories_map = {}
                    for i, row in enumerate(data):
                        (
                            pseudo,
                            slug,
                            photo,
                            description,
                            nblikes,
                            nbphotos,
                            nbvideos,
                            nbposts,
                            price,
                            website,
                            url,
                        ) = row.split(";")
                        sources_map[website] = sources_map.get(
                            website, Website.objects.get(slug=website)
                        )
                        profile = Profile.objects.create(
                            slug=slug,
                            pseudo=pseudo,
                            photo=photo,
                            description=description,
                            price=price,
                            url=url,
                            counts=Count.objects.create(
                                likes=nblikes,
                                photos=nbphotos,
                                videos=nbvideos,
                                posts=nbposts,
                            ),
                            website=sources_map[website],
                        )
                        for category_term in extract_categories(
                            description, flatten_terms
                        ):
                            id = flatten_terms_map[category_term]
                            categories_map[id] = categories_map.get(
                                id, Category.objects.get(id=id)
                            )
                            profile.categories.add(categories_map[id])
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
        payload = {"form": form, "subtitle": "Upload CSV for porn_models profiles"}
        context = self.admin_site.each_context(request)
        return render(
            request, "admin/porn_models/profile/csv_form.html", {**context, **payload}
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

    display_status.admin_order_field = "status"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("slug", "name_en", "name_fr", "synonyms")


@admin.register(Count)
class CountAdmin(admin.ModelAdmin):
    pass
