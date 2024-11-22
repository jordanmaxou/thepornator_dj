from django.urls import path
from .views import Out, OutWebsite

app_name = "out"

urlpatterns = [
    path("out/<site_slug>", OutWebsite.as_view(), name="out-view-site"),
    path("out/<type_out>_<id>", Out.as_view(), name="out-view"),
]
