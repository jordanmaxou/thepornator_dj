from django.urls import path
from .views import SurveyIndexView

app_name = "surveys"

urlpatterns = [
    path("site/survey.html", SurveyIndexView.as_view(), name="index"),
]
