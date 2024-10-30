from django.urls import path
from .views import StoryListView, StoryDetailView

app_name = "stories"

urlpatterns = [
    path("stories/", StoryListView.as_view(), name="index"),
    path("stories/<slug>.html", StoryDetailView.as_view(), name="content"),
]
