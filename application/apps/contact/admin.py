from django.contrib import admin

from apps.contact.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ("read",)
    list_display = ("email", "name", "subject", "message", "created_at", "read")
    ordering = (
        "read",
        "-created_at",
    )
    readonly_fields = ("name", "email", "subject", "message", "created_at")

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)

        if obj:
            obj.read = True
            obj.save(update_fields=["read"])

        return obj
