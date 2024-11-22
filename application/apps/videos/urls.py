from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [
    path("videos/", views.VideosIndexListView.as_view(), name="videos-index"),
    path(
        "videos/category/<category>.html",
        views.VideosCategoryListView.as_view(),
        name="videos-category",
    ),
    path(
        "videos/channel/<channel>.html",
        views.VideosChannelListView.as_view(),
        name="videos-channel",
    ),
    path(
        "webcamvideos/",
        views.WebcamVideosIndexListView.as_view(),
        name="webcam-videos-index",
    ),
    path(
        "webcamvideos/content/<slug>.html",
        views.WebcamVideosContentListView.as_view(),
        name="webcam-videos-content",
    ),
]
