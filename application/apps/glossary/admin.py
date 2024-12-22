from datetime import date

from django.contrib import admin
from django.utils.html import format_html

from apps.glossary.models import Glossary


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
            return queryset.filter(publication_date__lte=date.today())
        if self.value() == "unpublished":
            return queryset.filter(publication_date__gt=date.today())


@admin.register(Glossary)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "type", "lang", "display_publication_date")
    list_filter = (PublishedStatusFilter, "type", "lang")
    ordering = ("type", "lang", "slug")
    readonly_fields = ("count", "preview_picture")
    exclude = ("definition",)

    def preview_picture(self, obj):
        if len(obj.picture) > 0:
            return format_html(
                '<img src="{}" style="max-height:150px"/>'.format(obj.picture.url)
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
