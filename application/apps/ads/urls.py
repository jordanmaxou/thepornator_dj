from django.urls import path
from apps.ads import views

app_name = "ads"

urlpatterns = [
    path("banners/", views.BannerListView.as_view(), name="list"),
]
