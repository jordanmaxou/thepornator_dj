from django.contrib import admin

from apps.websites.models import Website, Category, Deal


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("slug", "name")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    pass
