from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = "blog"

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="index"),
    path("blog/<slug>.html", BlogDetailView.as_view(), name="content"),
]
