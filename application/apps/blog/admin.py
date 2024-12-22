from datetime import date

from django.contrib import admin

from tinymce.widgets import TinyMCE
from django.utils.html import format_html
from django.db.models import TextField

# from ckeditor.widgets import CKEditorWidget

from apps.blog.models import Blog


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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("slug", "title_en", "title_fr", "display_publication_date")
    ordering = ("-publication_date",)
    list_filter = (PublishedStatusFilter,)
    exclude = ("title", "content")
    formfield_overrides = {
        TextField: {"widget": TinyMCE},
    }

    def display_publication_date(self, obj):
        red, green = "#3C1518", "#69995D"
        if obj.publication_date > date.today():
            color = red
        else:
            color = green
        return format_html(
            f"<span style='background-color: {color};'>{obj.publication_date}</span>"
        )
