from django.urls import path
from .views import Out, VideoVoteUpdate

app_name = "out"

urlpatterns = [
    path("out/<type_out>_<id>", Out.as_view(), name="out-view"),
    path("video-vote-update/<id>", VideoVoteUpdate.as_view(), name="video-vote-update"),
]
