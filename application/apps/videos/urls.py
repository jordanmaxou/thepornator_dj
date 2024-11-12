from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [
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
