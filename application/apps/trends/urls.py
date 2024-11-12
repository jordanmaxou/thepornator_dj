from django.urls import path
from .views import TrendDetailView

app_name = "trends"

urlpatterns = [
    path("trends/<trend>.html", TrendDetailView.as_view(), name="trend"),
]
