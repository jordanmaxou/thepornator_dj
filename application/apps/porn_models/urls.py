from django.urls import path
from .views import (
    PornModelsIndexView,
    PornModelsSearchView,
    PornModelsCategoryView,
    PornModelsSiteView,
    PornModelsSiteCategoryView,
)

app_name = "porn_models"

urlpatterns = [
    path("models/", PornModelsIndexView.as_view(), name="index"),
    path("models/search.html", PornModelsSearchView.as_view(), name="search"),
    path(
        "models/category/<category>.html",
        PornModelsCategoryView.as_view(),
        name="category",
    ),
    path("models/site/<website>.html", PornModelsSiteView.as_view(), name="website"),
    path(
        "models/site/<website>/<category>.html",
        PornModelsSiteCategoryView.as_view(),
        name="website-category",
    ),
]
