from datetime import date
import json
from urllib.parse import urlencode, urljoin

from django.db.models.functions import Round
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _
from django.db.models import Count, Q, Avg, F
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings

from apps.ai_pictures.models import (
    Category,
    Content,
    AiOrNotAiScore,
    AiOrNotAiImage,
    Country,
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
        context["head"] = {
            "title": _("Free AI generated porn pictures - The Pornator"),
            "description": _(
                "All categories with AI generated porn pictures. Only porn images of women and men using artificial intelligence."
            ),
        }

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
        cat_map = {
            obj.pk: obj
            for obj in Category.objects.select_related("main_image_content").all()
        }
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
        context["head"] = {
            "title": _("Free AI generated %(category)s porn pictures - The Pornator")
            % {"category": context["custom_title"]},
            "description": _(
                "Watch free porn %(category)s pictures generated by IA. Only unique and hardcore pics on %(category)s category !"
            )
            % {"category": context["custom_title"]},
        }
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
        context["head"] = {
            "title": _("Free AI generated porn pictures by country - The Pornator"),
            "description": _(
                "All countries with AI generated porn pictures. All the porn photos were created using artificial intelligence."
            ),
        }
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = (
            qs.annotate(
                nb_contents=Count(
                    "content__id",
                    distinct=True,
                    filter=Q(
                        content__type=TypeOfContent.IMAGE,
                        content__publication_date__lte=date.today(),
                    ),
                )
            )
            .select_related("main_content")
            .filter(nb_contents__gt=0)
        )
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
        context["head"] = {
            "title": _("Free AI generated %(country)s porn pictures - The Pornator")
            % {"country": self.obj.name},
            "description": _(
                "Watch free porn %(country)s pictures generated by IA. Only unique and hardcore pics on %(country)s AI porn!"
            )
            % {"country": self.obj.name},
        }
        context["country"] = self.obj

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Country, slug=slug)

        return self.obj.content_set.filter(
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
        context["head"] = {
            "title": _("Free AI generated %(source)s porn pictures - The Pornator")
            % {"source": self.obj.name},
            "description": _(
                "Watch free porn %(source)s pictures generated by IA. Only women pictures of %(source)s source!"
            )
            % {"source": self.obj.name},
        }
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
    slug_field = "slug"

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
        context["head"] = {
            "title": _("%(title)s - Free AI generated porn picture")
            % {"title": self.object.title},
            "description": _(
                "Porn image %(title)s generated by AI. Original nude anime female character."
            )
            % {"title": self.object.title},
        }
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
        context["head"] = {
            "title": _("Game with real and AI-generated pornographic images"),
            "description": _(
                "Guess if the image is generated by AI or if it's a real photo. A quick and simple game where you just swipe left or right."
            ),
        }

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
        context["head"] = {
            "title": _("Free AI generated porn videos - The Pornator"),
            "description": _(
                "All categories with AI generated porn videos. Only porn videos of women using artificial intelligence."
            ),
        }
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
        cat_map = {
            obj.pk: obj
            for obj in Category.objects.select_related("main_video_content").all()
        }
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
        context["head"] = {
            "title": _("Free AI generated %(category)s porn videos - The Pornator")
            % {"category": self.obj.name},
            "description": _(
                "Watch free porn %(category)s videos generated by IA. Only women videos on %(category)s category !"
            )
            % {"category": self.obj.name},
        }
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
        context["custom_title"] = self.obj.slug.replace(".", "").capitalize()
        context["breadcrumbs"] = [
            {
                "label": _("AI Porn videos"),
                "link": reverse("ai_pictures:ai-porn-videos-index"),
            },
            {"label": context["custom_title"]},
        ]
        context["head"] = {
            "title": _("Free AI generated %(source)s porn videos - The Pornator")
            % {"source": context["custom_title"]},
            "description": _(
                "Watch free porn %(source)s videos generated by IA. Only women videos of %(source)s source!"
            )
            % {"source": context["custom_title"]},
        }
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
    slug_field = "slug"

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
        context["head"] = {
            "title": _("%(title)s - Free AI generated porn picture")
            % {"title": self.object.title},
            "description": _("Porn video %(title)s generated by AI.")
            % {"title": self.object.title},
        }
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
        content = get_object_or_404(Content, slug=slug)
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
        content = get_object_or_404(Content, slug=slug)
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
                    kwargs={"slug": next_content.slug},
                )
            else:
                next_url = reverse("home:home")

            return JsonResponse({"next_url": next_url})
        else:
            return HttpResponse(status=400)
