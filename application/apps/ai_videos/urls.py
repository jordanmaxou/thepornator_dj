from django.urls import path
from . import views

app_name = "ai_videos"

urlpatterns = [
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
    path("videos/", views.VideosIndexView.as_view(), name="videos-index"),
    path(
        "videos/category/<category>.html",
        views.VideosCategoryView.as_view(),
        name="videos-category",
    ),
    path(
        "videos/channel/<channel>.html",
        views.VideosChannelView.as_view(),
        name="videos-channel",
    ),
    path(
        "webcamvideos/",
        views.WebcamVideosIndexView.as_view(),
        name="webcam-videos-index",
    ),
    path(
        "webcamvideos/content/<slug>.html",
        views.WebcamVideosContentView.as_view(),
        name="webcam-videos-content",
    ),
]
