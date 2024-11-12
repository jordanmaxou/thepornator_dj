from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("_health", include("health_check.urls")),
    path("", include("apps.out.urls", namespace="out")),
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", include("apps.home.urls", namespace="home")),
    path("", include("apps.ai_pictures.urls", namespace="ai_pictures")),
    path("", include("apps.videos.urls", namespace="videos")),
    path("", include("apps.porn_models.urls", namespace="porn_models")),
    path("", include("apps.websites.urls", namespace="websites")),
    path("", include("apps.blog.urls", namespace="blog")),
    path("", include("apps.glossary.urls", namespace="glossary")),
    path("", include("apps.scripts.urls", namespace="scripts")),
    path("", include("apps.statistics.urls", namespace="statistics")),
    path("", include("apps.trends.urls", namespace="trends")),
    path("", include("apps.stories.urls", namespace="stories")),
    path("", include("apps.surveys.urls", namespace="surveys")),
    path("", include("apps.pages.urls", namespace="pages")),
)
