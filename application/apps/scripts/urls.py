from django.urls import path
from .views import ScriptListView, ScriptDetailView

app_name = "scripts"

urlpatterns = [
    path("script/", ScriptListView.as_view(), name="index"),
    path("script/content/<slug>.html", ScriptDetailView.as_view(), name="content"),
]
