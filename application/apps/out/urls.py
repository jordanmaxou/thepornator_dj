from django.urls import path
from .views import Out

app_name = "out"

urlpatterns = [
    path("out/<type_out>_<id>", Out.as_view(), name="out-view"),
]
