from functools import reduce
from datetime import date

from django.views.generic.base import TemplateView
from django.db.models import Avg, Count

from apps.trends.models import TrendingSearches
from apps.websites.models import Website
from apps.ai_pictures.models import Content, TypeOfContent
from apps.glossary.models import Glossary
from apps.porn_models.models import Profile
from apps.videos.models import Video
from apps.blog.models import Blog
from apps.stories.models import Story
from .utils import reduce_by_categories


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_type"] = "home"
        context["trends"] = TrendingSearches.objects.top_15()
        context["top_websites_by_categories"] = sorted(
            [
                category
                for category in reduce(
                    reduce_by_categories, Website.objects.by_category_avg_notes(), {}
                ).values()
            ],
            key=lambda c: c["position"],
        )
        context["most_recent_porn_sites"] = (
            Website.objects.annotate(
                avg_note_update=Avg("questionwebsite__note_update"),
            )
            .select_related("category")
            .order_by("creation_date")[:4]
        )
        context["most_recent_ai_pics"] = Content.objects.filter(
            type=TypeOfContent.IMAGE,
            country_id__isnull=False,
            image__isnull=False,
        ).order_by("-publication_date")[:4]

        context["most_recent_ai_videos"] = Content.objects.filter(
            type=TypeOfContent.VIDEO,
            image__isnull=False,
        ).order_by("-publication_date")[:4]

        context["lexicon_terms"] = Glossary.objects.order_by("-publication_date")[:4]

        model_of_the_day = (
            Profile.objects.annotate(category_nb=Count("categories"))
            .filter(category_nb__gt=0)
            .order_by("?")
            .first()
        )
        model_of_the_day.category = model_of_the_day.categories.first()
        context["model_of_the_day"] = model_of_the_day

        context["most_recent_porn_videos"] = (
            Video.objects.filter(enabled=True, publication_date__lte=date.today())
            .select_related("channel")
            .order_by("-publication_date")[:6]
        )

        context["most_recent_blogs"] = Blog.objects.filter(
            publication_date__lte=date.today()
        ).order_by("-publication_date")[:2]

        context["most_recent_stories"] = Story.objects.filter(
            publication_date__lte=date.today()
        ).order_by("-publication_date")[:2]

        return context
