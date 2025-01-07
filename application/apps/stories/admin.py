from datetime import date
from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.utils.html import format_html
from django.db.models import TextField

from tinymce.widgets import TinyMCE

from apps.stories.models import Story, Tag, Image


class ImageInlineFormset(BaseInlineFormSet):
    model = Image
    fields = ("file",)


class ImageInline(admin.StackedInline):
    model = Image
    formset = ImageInlineFormset
    extra = 1


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


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    exclude = ("title", "content")
    list_display = ("slug", "title_en", "author", "display_publication_date")
    list_filter = (PublishedStatusFilter, "author")
    formfield_overrides = {
        TextField: {"widget": TinyMCE},
    }
    inlines = (ImageInline,)

    def display_publication_date(self, obj):
        red, green = "#3C1518", "#69995D"
        if obj.publication_date > date.today():
            color = red
        else:
            color = green
        return format_html(
            f"<span style='background-color: {color};'>{obj.publication_date}</span>"
        )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name_en", "name_fr")
