from django.contrib import admin
from django.utils.html import format_html

from apps.glossary.models import Glossary


@admin.register(Glossary)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "type", "lang", "publication_date")
    list_filter = ("type", "lang")
    ordering = ("type", "lang", "slug")
    readonly_fields = ("count", "preview_picture")
    exclude = ("definition",)

    def preview_picture(self, obj):
        if len(obj.picture) > 0:
            return format_html(
                '<img src="{}" style="max-height:20px"/>'.format(obj.picture.url)
            )
