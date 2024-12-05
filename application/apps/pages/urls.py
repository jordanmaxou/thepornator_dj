from django.urls import path
from .views import AboutView, AdvertisingView

app_name = "pages"

urlpatterns = [
    path("info/about.html", AboutView.as_view(), name="about"),
    path("info/advertising.html", AdvertisingView.as_view(), name="advertising"),
]
