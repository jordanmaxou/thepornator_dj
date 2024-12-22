from django.contrib import admin
from django.utils.html import format_html

from apps.websites.models import Website, Category, Deal


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "display_icon", "end_date")
    exclude = ("description",)

    def display_icon(self, obj):
        if obj.icon:
            return format_html(
                '<img src="{}" style="max-height:45px"/>'.format(obj.icon.url)
            )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("slug", "name_en", "name_fr")


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("contact", "program", "start_date", "end_date", "status")
