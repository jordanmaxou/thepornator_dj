from django.urls import path
from apps.ai_pictures import views

app_name = "ai_pictures"

urlpatterns = [
    path("aiporn/", views.AiPornCategoryListView.as_view(), name="index"),
    path(
        "aiporn/aiornotai.html", views.AiPornAiOrNotAiView.as_view(), name="aiornotai"
    ),
    path(
        "aiporn/aiornotai/add",
        views.AiPornAiOrNotAddResultView.as_view(),
        name="aiornotai-add",
    ),
    path(
        "aiporn/category/<category>.html",
        views.AiPornCategoryContentListView.as_view(),
        name="category",
    ),
    path("aiporn/countries/", views.AiPornCountryListView.as_view(), name="countries"),
    path(
        "aiporn/countries/<country>.html",
        views.AiPornCountryContentListView.as_view(),
        name="country",
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
        "aiporn/content/<slug>/update",
        views.AiPornContentUpdateView.as_view(),
        name="content-update",
    ),
    path(
        "aiporn/content/<slug>/vote",
        views.AiPornContentVoteView.as_view(),
        name="content-vote",
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
