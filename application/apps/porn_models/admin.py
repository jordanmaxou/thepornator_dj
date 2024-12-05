from django.contrib import admin

from apps.porn_models.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pseudo",)
