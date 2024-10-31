from django.urls import path
from .views import ContactView, AboutView

app_name = "pages"

urlpatterns = [
    path("info/about.html", AboutView.as_view(), name="about"),
    path("info/contact.html", ContactView.as_view(), name="contact"),
]
