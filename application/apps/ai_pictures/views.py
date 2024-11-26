from datetime import date
import json
from urllib.parse import urlencode, urljoin

from django.db.models.functions import Round, Lower, Substr
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _
from django.db.models import Count, Q, Avg, F
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language
from django.http import HttpResponse, JsonResponse
from django.conf import settings

from apps.ai_pictures.models import (
    Category,
    Content,
    AiOrNotAiScore,
    AiOrNotAiImage,
    Country,
    Tag,
    TypeOfContent,
    Note,
)
from apps.websites.models import Website
from libs.request import get_client_ip


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
        context["page_type"] = "content-detail"
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
            "scary": self.object.note.scary / note_sum * 100 if note_sum > 0 else 0,
            "sexy": self.object.note.sexy / note_sum * 100 if note_sum > 0 else 0,
            "funny": self.object.note.funny / note_sum * 100 if note_sum > 0 else 0,
        }

        context["edit_url"] = reverse(
            "ai_pictures:content-update",
            kwargs={"slug": self.kwargs.get(self.slug_url_kwarg)},
        )

        context["vote_url"] = reverse(
            "ai_pictures:content-vote",
            kwargs={"slug": self.kwargs.get(self.slug_url_kwarg)},
        )

        return context

    def get_queryset(self):
        return self.model.objects.filter(
            type=TypeOfContent.IMAGE, publication_date__lte=date.today()
        )


class AiPornAiOrNotAiView(TemplateView):
    model = AiOrNotAiImage
    template_name = "ai_pictures/aiornotai.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_type"] = "ai-game"
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn pics"),
                "link": reverse("ai_pictures:index"),
            },
            {"label": _("AI or not AI game")},
        ]

        context["pictures"] = [
            {"id": row.id, "file": row.picture.url}
            for row in AiOrNotAiImage.objects.all()
        ]

        context["statistics"] = AiOrNotAiScore.objects.aggregate(
            total_quiz=Count("id"), avg_score=Round(Avg("score"), precision=2)
        )
        return context


class AiPornAiOrNotAddResultView(View):
    def post(self, request):
        user_responses = json.loads(request.body)
        truth = {
            p["id"]: p["is_real"]
            for p in AiOrNotAiImage.objects.filter(enabled=True).values("id", "is_real")
        }
        raw_score = 0
        for id, user_response in user_responses.items():
            if (truth[int(id)] is True and user_response == 1) or (
                truth[int(id)] is False and user_response == -1
            ):
                raw_score += 1
        score = round(raw_score * 20 / len(truth), 0)
        AiOrNotAiScore.objects.create(score=score, ip=get_client_ip(request))
        text = _(
            """I got a score of %(score)s/20 at @thepornator's quiz, at the game "Porn AI or not Porn AI?" and you?"""
            % {"score": score}
        )
        url = urljoin(settings.ALLOWED_HOSTS[0], reverse("ai_pictures:aiornotai"))
        return JsonResponse(
            {
                "score": score,
                "social_urls": {
                    "twitter": "{base}?{query}".format(
                        base=settings.BASE_TWITTER,
                        query=urlencode({"url": url, "text": text}),
                    ),
                    "facebook": "{base}?{query}".format(
                        base=settings.BASE_FACEBOOK,
                        query=urlencode({"url": url, "title": text}),
                    ),
                    "reddit": "{base}?{query}".format(
                        base=settings.BASE_REDDIT,
                        query=urlencode({"url": url, "title": text}),
                    ),
                },
            },
            status=201,
        )


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
        context["custom_title"] = self.obj.name
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
        context["page_type"] = "content-detail"
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn videos"),
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
            "scary": self.object.note.scary / note_sum * 100 if note_sum > 0 else 0,
            "sexy": self.object.note.sexy / note_sum * 100 if note_sum > 0 else 0,
            "funny": self.object.note.funny / note_sum * 100 if note_sum > 0 else 0,
        }

        context["edit_url"] = reverse(
            "ai_pictures:content-update",
            kwargs={"slug": self.kwargs.get(self.slug_url_kwarg)},
        )

        context["vote_url"] = reverse(
            "ai_pictures:content-vote",
            kwargs={"slug": self.kwargs.get(self.slug_url_kwarg)},
        )

        return context

    def get_queryset(self):
        return self.model.objects.filter(
            type=TypeOfContent.VIDEO, publication_date__lte=date.today()
        )


class AiPornContentUpdateView(View):
    def post(self, request, slug):
        data = json.loads(request.body)
        content = get_object_or_404(Content, code=slug)
        if (wanted_category_ids := data.get("categories")) and isinstance(
            wanted_category_ids, list
        ):
            content.categories.set(wanted_category_ids, clear=True)

        if "country" in data.keys():
            country_id = data.get("country")
            content.country_id = country_id
            content.save(update_fields=["country_id"])

        return HttpResponse(status=201)


class AiPornContentVoteView(View):
    def post(self, request, slug):
        data = json.loads(request.body)
        content = get_object_or_404(Content, code=slug)
        type_vote = data.get("vote")
        type_content = data.get("type")
        if type_vote in [
            "scary",
            "funny",
            "sexy",
            "next",
        ] and type_content in [TypeOfContent.IMAGE, TypeOfContent.VIDEO]:
            if type_vote != "next":
                if content.note is None:
                    content.note = Note.objects.create()
                    content.save(update_fields=["note"])

                Note.objects.filter(id=content.note.id).update(
                    **{type_vote: F(type_vote) + 1}
                )
            if next_content := content.next_content(type_content):
                next_url = reverse(
                    f"ai_pictures:{'content' if type_content == TypeOfContent.IMAGE else 'ai-porn-videos-content'}",
                    kwargs={"slug": next_content.code},
                )
            else:
                next_url = reverse("home:home")

            return JsonResponse({"next_url": next_url})
        else:
            return HttpResponse(status=400)
