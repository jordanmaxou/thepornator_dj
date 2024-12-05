from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps import views
from django.views.generic.base import TemplateView

from apps.pages.sitemap import StaticViewSitemap
from apps.websites.sitemap import WebsiteSitemap
from apps.ai_pictures.sitemap import AiPicturesSitemap, AiVideosSitemap
from apps.porn_models.sitemap import PornModelSitemap
from apps.glossary.sitemap import GlossarySitemap
from apps.videos.sitemap import VideosSitemap, WebcamvideosSitemap
from apps.scripts.sitemap import ScriptSitemap
from apps.blog.sitemap import BlogSitemap
from apps.stories.sitemap import StorySitemap
from apps.trends.sitemap import TrendsSitemap


sitemaps = {
    "statics": StaticViewSitemap,
    "sites": WebsiteSitemap,
    "ai": AiPicturesSitemap,
    "aivideos": AiVideosSitemap,
    "models": PornModelSitemap,
    "videos": VideosSitemap,
    "glossary": GlossarySitemap,
    "script": ScriptSitemap,
    "blog": BlogSitemap,
    "stories": StorySitemap,
    "trends": TrendsSitemap,
    "webcamvideos": WebcamvideosSitemap,
}
urlpatterns = [
    path("_health", include("health_check.urls")),
    path("", include("apps.out.urls", namespace="out")),
    path("", include("apps.ads.urls", namespace="ads")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap/index.xml",
        views.index,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.index",
    ),
    path(
        "sitemap/<section>.xml",
        views.sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", include("apps.home.urls", namespace="home")),
    path("", include("apps.ai_pictures.urls", namespace="ai_pictures")),
    path("", include("apps.videos.urls", namespace="videos")),
    path("", include("apps.porn_models.urls", namespace="porn_models")),
    path("", include("apps.surveys.urls", namespace="surveys")),
    path("", include("apps.statistics.urls", namespace="statistics")),
    path("", include("apps.websites.urls", namespace="websites")),
    path("", include("apps.blog.urls", namespace="blog")),
    path("", include("apps.glossary.urls", namespace="glossary")),
    path("", include("apps.scripts.urls", namespace="scripts")),
    path("", include("apps.trends.urls", namespace="trends")),
    path("", include("apps.stories.urls", namespace="stories")),
    path("", include("apps.pages.urls", namespace="pages")),
    path("", include("apps.contact.urls", namespace="contact")),
)

handler404 = "apps.pages.views.custom_404_view"
