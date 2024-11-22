from django.urls import path
from apps.ai_pictures import views

app_name = "ai_pictures"

urlpatterns = [
    path("aiporn/", views.AiPornCategoryListView.as_view(), name="index"),
    path(
        "aiporn/aiornotai.html", views.AiPornAiOrNotAiView.as_view(), name="aiornotai"
    ),
    path(
        "aiporn/<category>.html",
        views.AiPornCategoryContentListView.as_view(),
        name="category",
    ),
    path("aiporn/countries/", views.AiPornCountryListView.as_view(), name="countries"),
    path(
        "aiporn/countries/<country>.html",
        views.AiPornCountryContentListView.as_view(),
        name="country",
    ),
    path("aiporn/tags/", views.AiPornTagListView.as_view(), name="tags"),
    path(
        "aiporn/tags/<tag>.html", views.AiPornTagContentListView.as_view(), name="tag"
    ),
    path(
        "aiporn/source/<source>.html",
        views.AiPornSourceContentListView.as_view(),
        name="source",
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
