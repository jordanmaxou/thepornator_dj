from django.urls import path
from .views import (
    SurveyIndexView,
    AddSurveyView,
    ResultDetailView,
    UpdateSurveyToValidView,
)


app_name = "surveys"

urlpatterns = [
    path("site/survey.html", SurveyIndexView.as_view(), name="index"),
    path("site/survey/add", AddSurveyView.as_view(), name="add-survey"),
    path(
        "site/survey/valid/<slug>",
        UpdateSurveyToValidView.as_view(),
        name="valid-survey",
    ),
    path(
        "site/result/<slug>.html",
        ResultDetailView.as_view(),
        name="result",
    ),
]
