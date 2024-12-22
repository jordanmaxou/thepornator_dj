from django.contrib import admin

from apps.trends.models import TrendingSearches


@admin.register(TrendingSearches)
class TrendingSearchesAdmin(admin.ModelAdmin):
    list_display = ("request", "slug", "nb_result", "lang")
    list_filter = ("lang",)
    ordering = ("request",)
