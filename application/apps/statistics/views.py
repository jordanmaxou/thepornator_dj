import itertools
from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _
from django.db.models import (
    Count,
    Q,
    F,
    ExpressionWrapper,
    FloatField,
    Value,
    Sum,
    Case,
    When,
)
from django.db.models.functions import TruncDate

from apps.surveys.models import Survey
from apps.websites.models import Website
from apps.porn_models.models import Profile
from apps.ai_pictures.models import Note, AiOrNotAiScore
from apps.videos.models import Video, Count as VideoCount

COLORS = [
    "#4dc9f6",
    "#f67019",
    "#f53794",
    "#537bc4",
    "#acc236",
    "#166a8f",
    "#00a950",
    "#58595b",
    "#8549ba",
    "#FF49ba",
]


class StatisticsView(TemplateView):
    template_name = "statistics/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [{"label": _("All Pornator's stats")}]
        context["head"] = {
            "title": _("All Pornator's stats"),
            "description": _(
                "All the Pornator statistics to know everything about the transparency in the use and the relevance of the application's results - The Pornator"
            ),
        }
        context["page_type"] = "statistics"

        surveys_by_day = (
            Survey.objects.annotate(truncated_date=TruncDate("creation_date"))
            .values("truncated_date")
            .annotate(nb=Count("id"))
            .order_by("truncated_date")
            .values_list("truncated_date", "nb")
        )
        surveys_by_day_labels, surveys_by_day_data = list(zip(*surveys_by_day))
        context["surveys_by_days"] = {
            "total": Survey.objects.count(),
            "data": {
                "labels": surveys_by_day_labels,
                "data": surveys_by_day_data,
                "title": _("Number of completed surveys per day"),
            },
        }

        surveys_reliability_by_day = (
            Survey.objects.annotate(truncated_date=TruncDate("creation_date"))
            .values("truncated_date")
            .annotate(
                positive=Count("is_valid", filter=Q(is_valid=True)),
                total=Count("is_valid", filter=Q(is_valid__isnull=False)),
            )
            .annotate(
                rate=Case(
                    When(
                        total__gt=0,
                        then=ExpressionWrapper(
                            F("positive") * 100.0 / F("total"),
                            output_field=FloatField(),
                        ),
                    ),
                    default=Value(0.0),
                )
            )
            .order_by("truncated_date")
            .values_list("truncated_date", "rate")
        )
        surveys_reliability_by_day_labels, surveys_reliability_by_day_data = list(
            zip(*surveys_reliability_by_day)
        )
        context["reliability_by_days_data"] = {
            "labels": surveys_reliability_by_day_labels,
            "data": surveys_reliability_by_day_data,
            "title": _("Evolution of the reliability per day"),
        }

        top_10_websites_total = Survey.objects.count()
        top_10_websites = [
            (f"{survey[0]} ({round(survey[1], 2)}%)", survey[1])
            for survey in Survey.objects.values("selected_websites__first__name")
            .annotate(
                rate=ExpressionWrapper(
                    Count("id")
                    * 100.0
                    / Value(top_10_websites_total, output_field=FloatField()),
                    output_field=FloatField(),
                )
            )
            .order_by("-rate")
            .values_list("selected_websites__first__name", "rate")[:10]
        ]
        top_10_websites_labels, top_10_websites_data = list(zip(*top_10_websites))
        context["surveys_best_website_results_data"] = {
            "labels": top_10_websites_labels,
            "data": top_10_websites_data,
            "title": _("Top 10 breakdown of gross results by site"),
            "colors": list(
                itertools.islice(itertools.cycle(COLORS), len(top_10_websites))
            ),
        }

        most_clicked_websites = (
            Website.objects.values("name", "click")
            .order_by("-click")
            .values_list("name", "click")[:10]
        )
        most_clicked_websites_labels, most_clicked_websites_data = list(
            zip(*most_clicked_websites)
        )
        context["nb_clicks_by_site_data"] = {
            "labels": most_clicked_websites_labels,
            "label": "",
            "title": _("Number of clicks"),
            "data": most_clicked_websites_data,
        }

        most_clicked_models = (
            (f"{i+1}/ {profile[1]} > {profile[0]}", profile[2])
            for i, profile in enumerate(
                Profile.objects.values("pseudo", "counts__clicks")
                .order_by("-counts__clicks")
                .values_list("pseudo", "website__name", "counts__clicks")[:10]
            )
        )
        most_clicked_models_labels, most_clicked_models_data = list(
            zip(*most_clicked_models)
        )
        context["nb_clicks_by_model_data"] = {
            "labels": most_clicked_models_labels,
            "label": "",
            "title": _("Number of clicks"),
            "data": most_clicked_models_data,
        }

        votes = Note.objects.aggregate(
            nb_sexy=Sum("sexy"), nb_funny=Sum("funny"), nb_scary=Sum("scary")
        )
        total_votes = sum(votes.values())
        pictures_total = Note.objects.count()
        pictures_with_votes = (
            pictures_total - Note.objects.filter(sexy=0, funny=0, scary=0).count()
        )
        context["aiporn_picture_classification"] = {
            "total_vote": total_votes,
            "pictures_with_votes": pictures_with_votes,
            "pictures_total": pictures_total,
            "picture_with_votes_rate": round(
                pictures_with_votes * 100 / pictures_total, 2
            ),
            "extended_labels": {
                "sexy": _("Sexy")
                + f" {votes['nb_sexy']} ({round(votes['nb_sexy'] * 100 / total_votes, 2)}%)",
                "funny": _("Funny")
                + f" {votes['nb_funny']} ({round(votes['nb_funny'] * 100 / total_votes, 2)}%)",
                "scary": _("Scary")
                + f" {votes['nb_scary']} ({round(votes['nb_scary'] * 100 / total_votes, 2)}%)",
            },
            "data": {
                "labels": [
                    _("Sexy"),
                    _("Funny"),
                    _("Scary"),
                ],
                "label": "",
                "title": _("AI porn pictures qualification"),
                "data": [votes["nb_sexy"], votes["nb_funny"], votes["nb_scary"]],
                "colors": list(itertools.islice(itertools.cycle(COLORS), 3)),
            },
        }

        quiz_per_day = (
            AiOrNotAiScore.objects.annotate(truncated_date=TruncDate("date"))
            .values("truncated_date")
            .annotate(nb=Count("id"))
            .order_by("truncated_date")
            .values_list("truncated_date", "nb")
        )
        quiz_per_day_labels, quiz_per_day_data = list(zip(*quiz_per_day))
        context["ai_or_not_ai_by_date"] = {
            "total": AiOrNotAiScore.objects.count(),
            "data": {
                "labels": quiz_per_day_labels,
                "label": "",
                "title": _('Number of "AI or Not AI" quiz per day'),
                "data": quiz_per_day_data,
            },
        }

        nb_clicks_by_channel = (
            Video.objects.values("channel__name")
            .annotate(nb=Sum("counts__clicks"))
            .order_by("-nb")
            .values_list("channel__name", "nb")[:10]
        )
        nb_clicks_by_channel_labels, nb_clicks_by_channel_data = list(
            zip(*nb_clicks_by_channel)
        )
        context["nb_clicks_by_channel"] = {
            "total": sum(nb_clicks_by_channel_data),
            "data": {
                "labels": [
                    f"{i+1}/ {label}"
                    for i, label in enumerate(nb_clicks_by_channel_labels)
                ],
                "label": "",
                "title": _("Number of clicks"),
                "data": nb_clicks_by_channel_data,
            },
        }

        total_videos = Video.objects.count()
        votes_videos = Video.objects.filter(
            Q(counts__up__gt=0) | Q(counts__down__gt=0)
        ).count()
        votes = VideoCount.objects.aggregate(like=Sum("up"), dislike=Sum("down"))
        context["video_classification"] = {
            "total_videos": total_videos,
            "votes_videos": votes_videos,
            "votes_videos_rate": round(votes_videos * 100 / total_videos, 2),
            "total_votes": sum(votes.values()),
            "extended_labels": {
                "like": _("I like")
                + ":"
                + f" {votes['like']} ({round(votes['like'] * 100 / total_votes, 2)}%)",
                "dislike": _("I dislike")
                + ":"
                + f" {votes['dislike']} ({round(votes['dislike'] * 100 / total_votes, 2)}%)",
            },
            "data": {
                "labels": ["👍", "👎"],
                "label": "",
                "title": _("Porn video rates"),
                "data": [votes["like"], votes["dislike"]],
            },
        }

        return context
