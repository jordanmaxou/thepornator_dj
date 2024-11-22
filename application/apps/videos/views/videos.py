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
        cat_map = {obj.pk: obj for obj in Category.objects.all()}
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
        context["category"] = self.obj

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Category, slug=slug)

        return self.obj.video_set.filter(publication_date__lte=date.today())


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
        context["channel"] = self.obj

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Channel, slug=slug)

        return self.obj.video_set.filter(publication_date__lte=date.today())
