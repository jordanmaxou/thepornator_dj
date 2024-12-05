from django.urls import path
from .views import GlossaryDetailView, GlossaryListView, GlossaryVoteView

app_name = "glossary"

urlpatterns = [
    path("glossary/", GlossaryListView.as_view(), name="index"),
    path("glossary/<term>/vote", GlossaryVoteView.as_view(), name="vote"),
    path("glossary/<term>.html", GlossaryDetailView.as_view(), name="content"),
]
