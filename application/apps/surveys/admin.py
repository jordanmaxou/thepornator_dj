from django.contrib import admin

from apps.surveys.models import (
    Survey,
    Podium,
    Question,
    Theme,
)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = (
        "user_daily_fingerprint",
        "is_valid",
        "selected_websites",
        "creation_date",
    )
    readonly_fields = ("selected_websites",)
    ordering = ("-creation_date",)


@admin.register(Podium)
class PodiumAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    exclude = ("sentence",)
    list_display = ("sentence_en", "sentence_fr", "theme", "position")


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    exclude = ("name",)
    list_display = ("id", "name_en", "name_fr")
