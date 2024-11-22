from datetime import date

from django.db.models.functions import Round, Lower, Substr
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _
from django.db.models import Count, Q, Avg
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language

from apps.ai_pictures.models import (
    Category,
    Content,
    AiOrNotAi,
    Country,
    Tag,
    TypeOfContent,
)
from apps.websites.models import Website


class AiPornCategoryListView(ListView):
    template_name = "ai_pictures/index.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [{"label": _("AI Porn pics")}]

        context["contents_by_source"] = (
            Website.objects.annotate(
                nb_contents=Count(
                    "content__id",
                    distinct=True,
                    filter=Q(
                        content__publication_date__lte=date.today(),
                        content__type=TypeOfContent.IMAGE,
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
                    "content__id",
                    distinct=True,
                    filter=Q(
                        content__publication_date__lte=date.today(),
                        content__type=TypeOfContent.IMAGE,
                    ),
                ),
            )
            .filter(nb_contents__gt=0)
            .order_by("name")
            .values("id", "slug", "name", "nb_contents")
        )
        for category in categories:
            category["main_content"] = cat_map[category["id"]].main_image_content

        return categories


class AiPornCategoryContentListView(ListView):
    template_name = "ai_pictures/category.html"
    context_object_name = "contents"
    slug_url_kwarg = "category"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug in ["latest", "sexiest", "scariest", "funniest"]:
            slug_title = {
                "latest": _("The latest published"),
                "sexiest": _("The sexiest"),
                "scariest": _("The scariest"),
                "funniest": _("The funniest"),
            }
            context["custom_title"] = slug_title.get(slug)
        else:
            context["custom_title"] = self.obj.name

        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {"label": context["custom_title"]},
        ]
        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug in ["latest", "sexiest", "scariest", "funniest"]:
            result = Content.objects.filter(
                type=TypeOfContent.IMAGE, publication_date__lte=date.today()
            )

            if slug == "latest":
                return result.order_by("-publication_date")
            else:
                m = {"sexiest": "sexy", "funniest": "funny", "scariest": "scary"}
                return result.order_by(f"-note__{m[slug]}")

        self.obj = get_object_or_404(Category, slug=slug)

        return self.obj.content_set.filter(
            type=TypeOfContent.IMAGE, publication_date__lte=date.today()
        )


class AiPornCountryListView(ListView):
    model = Country
    context_object_name = "countries"
    template_name = "ai_pictures/countries.html"
    ordering = "name"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {"label": _("Countries")},
        ]

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(
            nb_contents=Count(
                "content__id",
                distinct=True,
                filter=Q(
                    content__type=TypeOfContent.IMAGE,
                    content__publication_date__lte=date.today(),
                ),
            )
        ).filter(nb_contents__gt=0)
        return qs


class AiPornCountryContentListView(ListView):
    template_name = "ai_pictures/country.html"
    context_object_name = "contents"
    slug_url_kwarg = "country"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {
                "label": _("Countries"),
                "link": reverse("ai_pictures:countries"),
            },
            {"label": self.obj.name},
        ]
        context["country"] = self.obj

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Country, slug=slug)

        return self.obj.content_set.filter(
            type=TypeOfContent.IMAGE, publication_date__lte=date.today()
        )


class AiPornTagListView(ListView):
    template_name = "ai_pictures/tags.html"
    context_object_name = "tags"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {
                "label": _("All tags"),
            },
        ]

        return context

    def get_queryset(self):
        return Tag.objects.filter(lang=get_language()).annotate(
            nb_contents=Count(
                "contents__id",
                distinct=True,
                filter=Q(
                    contents__type=TypeOfContent.IMAGE,
                    contents__publication_date__lte=date.today(),
                ),
            ),
            first_letter=Lower(Substr("name", 1, 1)),
        )


class AiPornTagContentListView(ListView):
    template_name = "ai_pictures/tag.html"
    slug_url_kwarg = "tag"
    context_object_name = "contents"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {
                "label": _("All tags"),
                "link": reverse("ai_pictures:tags"),
            },
            {"label": self.obj.name},
        ]
        context["tag"] = self.obj

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Tag, slug=slug)

        return self.obj.contents.filter(
            type=TypeOfContent.IMAGE, publication_date__lte=date.today()
        )


class AiPornSourceContentListView(ListView):
    template_name = "ai_pictures/source.html"
    context_object_name = "contents"
    slug_url_kwarg = "source"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {"label": self.obj.name},
        ]
        context["source"] = (
            Website.objects.filter(pk=self.obj.pk)
            .annotate(
                avg_note_update=Avg("questionwebsite__note_update"),
            )
            .first()
        )

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Website, slug=slug)

        return self.obj.content_set.filter(
            type=TypeOfContent.IMAGE, publication_date__lte=date.today()
        ).order_by("-note__sexy")


class AiPornContentView(DetailView):
    model = Content
    template_name = "ai_pictures/content.html"
    context_object_name = "content"
    slug_field = "code"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {"label": self.object.title[:20]},
        ]
        context["related_content"] = (
            Content.objects.exclude(id=self.object.id)
            .filter(
                categories__in=self.object.categories.all(),
                type=TypeOfContent.IMAGE,
                publication_date__lte=date.today(),
            )
            .annotate(
                shared_categories=Count(
                    "categories",
                    filter=Q(categories__in=self.object.categories.all()),
                )
            )
            .order_by("-shared_categories")
        )[:18]

        note_sum = sum(
            [self.object.note.scary, self.object.note.sexy, self.object.note.funny]
        )
        context["notes"] = {
            "scary": self.object.note.scary / note_sum * 100,
            "sexy": self.object.note.sexy / note_sum * 100,
            "funny": self.object.note.funny / note_sum * 100,
        }
        return context

    def get_queryset(self):
        return self.model.objects.filter(
            type=TypeOfContent.IMAGE, publication_date__lte=date.today()
        )


class AiPornAiOrNotAiView(TemplateView):
    template_name = "ai_pictures/aiornotai.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {"label": _("AI or not AI game")},
        ]

        context["statistics"] = AiOrNotAi.objects.aggregate(
            total_quiz=Count("id"), avg_score=Round(Avg("score"), precision=2)
        )
        return context


class AiPornVideosIndexView(ListView):
    template_name = "ai_pictures/aipornvideos/index.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [{"label": _("AI Porn videos")}]

        context["contents_by_source"] = (
            Website.objects.annotate(
                nb_contents=Count(
                    "content__id",
                    distinct=True,
                    filter=Q(
                        content__publication_date__lte=date.today(),
                        content__type=TypeOfContent.VIDEO,
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
                    "content__id",
                    distinct=True,
                    filter=Q(
                        content__publication_date__lte=date.today(),
                        content__type=TypeOfContent.VIDEO,
                    ),
                ),
            )
            .filter(nb_contents__gt=0)
            .order_by("name")
            .values("id", "slug", "name", "nb_contents")
        )
        for category in categories:
            category["main_content"] = cat_map[category["id"]].main_video_content

        return categories


class AiPornVideosCategoryView(ListView):
    template_name = "ai_pictures/aipornvideos/category.html"
    context_object_name = "contents"
    slug_url_kwarg = "category"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn videos"),
                "link": reverse("ai_pictures:ai-porn-videos-index"),
            },
            {"label": self.obj.name},
        ]
        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Category, slug=slug)

        return self.obj.content_set.filter(
            type=TypeOfContent.VIDEO, publication_date__lte=date.today()
        )


class AiPornVideosSourceView(ListView):
    template_name = "ai_pictures/aipornvideos/source.html"
    context_object_name = "contents"
    slug_url_kwarg = "source"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn videos"),
                "link": reverse("ai_pictures:ai-porn-videos-index"),
            },
            {"label": self.obj.name},
        ]
        context["source"] = (
            Website.objects.filter(pk=self.obj.pk)
            .annotate(
                avg_note_update=Avg("questionwebsite__note_update"),
                reviews=Count("survey", distinct=True, filter=Q(survey__is_valid=True)),
            )
            .first()
        )

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Website, slug=slug)

        return self.obj.content_set.filter(
            type=TypeOfContent.VIDEO, publication_date__lte=date.today()
        ).order_by("-note__sexy")


class AiPornVideosContentView(DetailView):
    model = Content
    template_name = "ai_pictures/aipornvideos/content.html"
    context_object_name = "content"
    slug_field = "code"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:ai-porn-videos-index"),
            },
            {"label": self.object.title[:20]},
        ]
        context["related_content"] = (
            Content.objects.exclude(id=self.object.id)
            .filter(
                categories__in=self.object.categories.all(),
                type=TypeOfContent.VIDEO,
                publication_date__lte=date.today(),
            )
            .annotate(
                shared_categories=Count(
                    "categories",
                    filter=Q(categories__in=self.object.categories.all()),
                )
            )
            .order_by("-shared_categories")
        )[:18]

        note_sum = sum(
            [self.object.note.scary, self.object.note.sexy, self.object.note.funny]
        )
        context["notes"] = {
            "scary": self.object.note.scary / note_sum * 100,
            "sexy": self.object.note.sexy / note_sum * 100,
            "funny": self.object.note.funny / note_sum * 100,
        }
        return context

    def get_queryset(self):
        return self.model.objects.filter(
            type=TypeOfContent.VIDEO, publication_date__lte=date.today()
        )
