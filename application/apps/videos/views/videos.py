from datetime import date

from django.views.generic import ListView
from django.db.models import Count, Q
from django.utils.translation import gettext as _
from django.urls import reverse
from django.shortcuts import get_object_or_404

from apps.videos.models import Category, Channel


class VideosIndexListView(ListView):
    template_name = "videos/videos/index.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [{"label": _("Porn videos")}]
        context["head"] = {
            "title": _("Porn videos search engine - The Pornator"),
            "description": _(
                "This videos search engine is a free porn collection of hottest porn. Please find your content by category or channel. Thousands of daily updates."
            ),
        }
        context["contents_by_channel"] = (
            Channel.objects.annotate(
                nb_contents=Count(
                    "video__id",
                    distinct=True,
                    filter=Q(
                        video__enabled=True,
                        video__publication_date__lte=date.today(),
                    ),
                )
            )
            .filter(nb_contents__gt=0)
            .order_by("-nb_contents")
        )
        return context

    def get_queryset(self):
        cat_map = {
            obj.pk: obj for obj in Category.objects.select_related("main_content").all()
        }
        categories = list(
            Category.objects.annotate(
                nb_contents=Count(
                    "video__id",
                    distinct=True,
                    filter=Q(
                        video__enabled=True,
                        video__publication_date__lte=date.today(),
                    ),
                ),
            )
            .filter(nb_contents__gt=0)
            .order_by("name")
            .values("id", "slug", "name", "nb_contents")
        )
        for category in categories:
            category["main_content"] = cat_map[category["id"]].main_content

        return categories


class VideosCategoryListView(ListView):
    template_name = "videos/videos/category.html"
    context_object_name = "videos"
    slug_url_kwarg = "category"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Porn videos"),
                "link": reverse("videos:videos-index"),
            },
            {"label": self.obj.name},
        ]
        context["head"] = {
            "title": _("List of %(category)s porn videos - The Pornator")
            % {"category": self.obj.name},
            "description": _(
                "Watch %(category)s porn videos without misleading links. Search engine for %(category)s content on premium tubes."
            )
            % {"category": self.obj.name},
        }
        context["category"] = self.obj
        context["page_type"] = "porn-videos-tubes"

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Category, slug=slug)

        return self.obj.video_set.select_related("channel").filter(
            publication_date__lte=date.today()
        )


class VideosChannelListView(ListView):
    template_name = "videos/videos/channel.html"
    context_object_name = "videos"
    slug_url_kwarg = "channel"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Porn videos"),
                "link": reverse("videos:videos-index"),
            },
            {"label": self.obj.name},
        ]
        context["head"] = {
            "title": _("List of %(source)s porn videos - The Pornator")
            % {"source": self.obj.name},
            "description": _(
                "Watch %(source)s porn videos without misleading links. Search engine for %(source)s content on premium tubes."
            )
            % {"source": self.obj.name},
        }
        context["channel"] = self.obj
        context["page_type"] = "porn-videos-tubes"

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Channel, slug=slug)

        return self.obj.video_set.filter(publication_date__lte=date.today())
