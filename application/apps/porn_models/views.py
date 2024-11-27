from django.views.generic import ListView
from django.utils.translation import gettext as _
from django.db.models import Count, Q
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchVector
from django.utils.translation import get_language
from django.conf import settings

from apps.porn_models.models import Category, Website, Profile
from apps.trends.models import TrendingSearches


class PornModelsIndexView(ListView):
    template_name = "porn_models/index.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [{"label": _("Performers search engine")}]
        context["websites"] = (
            Website.objects.annotate(
                nb_profiles=Count(
                    "profile__id",
                    distinct=True,
                )
            )
            .filter(nb_profiles__gt=0)
            .order_by("-nb_profiles")
        )
        return context

    def get_queryset(self):
        cat_map = {obj.pk: obj for obj in Category.objects.all()}
        categories = list(
            Category.objects.annotate(
                nb_profiles=Count(
                    "profile__id",
                    distinct=True,
                ),
            )
            .filter(nb_profiles__gt=0)
            .order_by("name")
            .values("id", "slug", "name", "nb_profiles")
        )
        for category in categories:
            category["main_profile"] = cat_map[category["id"]].main_profile

        return categories


class PornModelsSearchView(ListView):
    model = Profile
    template_name = "porn_models/search.html"
    context_object_name = "profiles"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("query")
        title = _("Results") + f" {query}"
        context["breadcrumbs"] = [
            {
                "label": _("Performers search engine"),
                "link": reverse("porn_models:index"),
            },
            {"label": title},
        ]
        context["title"] = title

        if (
            self.queryset.count() > 0
            and (query := self.query.strip())
            and len(query) > 0
        ):
            TrendingSearches.objects.create(
                request=self.query, lang=get_language(), nb_result=self.queryset.count()
            )

        return context

    def get_queryset(self):
        query = self.request.GET.get("query")
        if self.query in settings.WORD_BLACK_LIST:
            return super().get_queryset().none()
        qs = super().get_queryset()
        qs = qs.annotate(
            search=SearchVector(
                "pseudo", "description", "categories__name", "website__name"
            )
        ).filter(search=query)
        self.queryset = qs
        return qs


class PornModelsCategoryView(ListView):
    template_name = "porn_models/site-category.html"
    context_object_name = "profiles"
    slug_url_kwarg = "category"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Performers search engine"),
                "link": reverse("porn_models:index"),
            },
            {"label": self.obj.name},
        ]
        context["category"] = self.obj
        context["title"] = self.obj.name

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Category, slug=slug)
        return self.obj.profile_set.all()


class PornModelsSiteView(ListView):
    template_name = "porn_models/site.html"
    context_object_name = "profiles"
    slug_url_kwarg = "website"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Performers search engine"),
                "link": reverse("porn_models:index"),
            },
            {"label": self.obj.name},
        ]
        if self.obj.slug == "onlyfans":
            context["page_type"] = "onlyfans-profiles"

        context["website"] = self.obj
        context["title"] = self.obj.name
        context["categories"] = Category.objects.filter(
            profile__website__id=self.obj.id
        ).annotate(
            nb_profiles=Count(
                "profile__id", distinct=True, filter=Q(profile__website__id=self.obj.id)
            )
        )

        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        self.obj = get_object_or_404(Website, slug=slug)
        return self.obj.profile_set.all()


class PornModelsSiteCategoryView(ListView):
    template_name = "porn_models/site-category.html"
    context_object_name = "profiles"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Performers search engine"),
                "link": reverse("porn_models:index"),
            },
            {
                "label": self.website.name,
                "link": reverse(
                    "porn_models:website", kwargs={"website": self.website.slug}
                ),
            },
            {"label": self.category.name},
        ]

        context["title"] = f"{self.website.name} {self.category.name}"

        return context

    def get_queryset(self):
        website_slug = self.kwargs.get("website")
        category_slug = self.kwargs.get("category")
        self.website = get_object_or_404(Website, slug=website_slug)
        self.category = get_object_or_404(Category, slug=category_slug)

        return self.website.profile_set.filter(categories=self.category)
