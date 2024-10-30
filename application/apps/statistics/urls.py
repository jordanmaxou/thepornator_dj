from django.urls import path
from .views import StatisticsView

app_name = "statistics"

urlpatterns = [
    path("site/stats.html", StatisticsView.as_view(), name="index"),
]
