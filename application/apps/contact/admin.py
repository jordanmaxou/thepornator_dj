from django.contrib import admin

from apps.contact.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "subject", "message", "created_at")
    ordering = ("-created_at",)
