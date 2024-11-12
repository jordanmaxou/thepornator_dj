from django.urls import path
from apps.ai_pictures import views

app_name = "ai_pictures"

urlpatterns = [
    path("aiporn/", views.AiPornIndexView.as_view(), name="index"),
    path("aiporn/<category>.html", views.AiPornCategoryView.as_view(), name="category"),
    path("aiporn/countries/", views.AiPornCountriesView.as_view(), name="countries"),
    path(
        "aiporn/countries/<country>.html",
        views.AiPornCountryView.as_view(),
        name="country",
    ),
    path("aiporn/tags/", views.AiPornTagsView.as_view(), name="tags"),
    path("aiporn/tags/<tag>.html", views.AiPornTagView.as_view(), name="tag"),
    path(
        "aiporn/source/<source>.html", views.AiPornSourceView.as_view(), name="source"
    ),
    path(
        "aiporn/aiornotai.html", views.AiPornAiOrNotAiView.as_view(), name="aiornotai"
    ),
    path(
        "aiporn/content/<slug>.html", views.AiPornContentView.as_view(), name="content"
    ),
    path(
        "aipornvideos/",
        views.AiPornVideosIndexView.as_view(),
        name="ai-porn-videos-index",
    ),
    path(
        "aipornvideos/category/<category>.html",
        views.AiPornVideosCategoryView.as_view(),
        name="ai-porn-videos-category",
    ),
    path(
        "aipornvideos/source/<source>.html",
        views.AiPornVideosSourceView.as_view(),
        name="ai-porn-videos-source",
    ),
    path(
        "aipornvideos/content/<slug>.html",
        views.AiPornVideosContentView.as_view(),
        name="ai-porn-videos-content",
    ),
]
