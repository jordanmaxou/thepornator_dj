from django.urls import path
from .views import WebsiteCategoryListView, WebsiteSiteDetailView

app_name = "websites"

urlpatterns = [
    path(
        "category/<category>.html", WebsiteCategoryListView.as_view(), name="category"
    ),
    path("site/<website>.html", WebsiteSiteDetailView.as_view(), name="site"),
]
