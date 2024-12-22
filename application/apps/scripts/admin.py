from django.contrib import admin

from apps.scripts.models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass
