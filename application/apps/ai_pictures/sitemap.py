from datetime import date

from django.contrib.sitemaps import Sitemap
from django.db.models import Q, Count
from django.urls import reverse

from apps.ai_pictures.models import Content, Country, Category, TypeOfContent
from apps.websites.models import Website


class AiSitemap(Sitemap):
    TYPE_OF_CONTENT: TypeOfContent
    i18n = True
    protocol = "https"

    def items(self):
        return (
            list(
                Content.objects.filter(
                    type=self.TYPE_OF_CONTENT, publication_date__lte=date.today()
                )
            )
            + list(
                Category.objects.annotate(
                    nb_contents=Count(
                        "content__id",
                        distinct=True,
                        filter=Q(
                            content__publication_date__lte=date.today(),
                            content__type=self.TYPE_OF_CONTENT,
                        ),
                    )
                ).filter(nb_contents__gt=0)
            )
            + list(
                Website.objects.annotate(
                    nb_contents=Count(
                        "content__id",
                        distinct=True,
                        filter=Q(
                            content__publication_date__lte=date.today(),
                            content__type=self.TYPE_OF_CONTENT,
                        ),
                    )
                ).filter(nb_contents__gt=0)
            )
        )

    def lastmod(self, obj):
        if hasattr(obj, "last_update"):
            return obj.last_update.date()
        elif isinstance(obj, dict):
            return obj["lastmod"]
        return date.today()

    def location(self, obj):
        if isinstance(obj, dict):
            return obj["location"]
        else:
            return super().location(obj)

    def priority(self, obj):
        if isinstance(obj, dict):
            return obj["priority"]
        else:
            return 1

    def changefreq(self, obj):
        if isinstance(obj, dict):
            return obj["changefreq"]
        return "weekly"


class AiPicturesSitemap(AiSitemap):
    TYPE_OF_CONTENT = TypeOfContent.IMAGE

    def items(self):
        return [
            *super().items(),
            *list(
                Country.objects.annotate(
                    nb_contents=Count(
                        "content__id",
                        distinct=True,
                        filter=Q(
                            content__publication_date__lte=date.today(),
                            content__type=self.TYPE_OF_CONTENT,
                        ),
                    )
                ).filter(nb_contents__gt=0)
            ),
            *[
                {
                    "location": reverse("ai_pictures:index"),
                    "changefreq": "daily",
                    "priority": 0.5,
                    "lastmod": date.today(),
                },
                {
                    "location": reverse(
                        "ai_pictures:category", kwargs={"category": "latest"}
                    ),
                    "changefreq": "daily",
                    "priority": 0.5,
                    "lastmod": date.today(),
                },
                {
                    "location": reverse(
                        "ai_pictures:category", kwargs={"category": "sexiest"}
                    ),
                    "changefreq": "daily",
                    "priority": 0.5,
                    "lastmod": date.today(),
                },
                {
                    "location": reverse(
                        "ai_pictures:category", kwargs={"category": "scariest"}
                    ),
                    "changefreq": "daily",
                    "priority": 0.5,
                    "lastmod": date.today(),
                },
                {
                    "location": reverse(
                        "ai_pictures:category", kwargs={"category": "funniest"}
                    ),
                    "changefreq": "daily",
                    "priority": 0.5,
                    "lastmod": date.today(),
                },
                {
                    "location": reverse("ai_pictures:aiornotai"),
                    "changefreq": "daily",
                    "priority": 0.5,
                    "lastmod": date.today(),
                },
                {
                    "location": reverse("ai_pictures:countries"),
                    "changefreq": "daily",
                    "priority": 0.5,
                    "lastmod": date.today(),
                },
            ],
        ]

    def location(self, obj):
        if isinstance(obj, dict):
            return obj["location"]
        elif isinstance(obj, Website):
            return reverse("ai_pictures:source", kwargs={"source": obj.slug})
        else:
            return super().location(obj)


class AiVideosSitemap(AiSitemap):
    TYPE_OF_CONTENT = TypeOfContent.VIDEO

    def items(self):
        return [
            *super().items(),
            *[
                {
                    "location": reverse("ai_pictures:ai-porn-videos-index"),
                    "changefreq": "daily",
                    "priority": 0.5,
                    "lastmod": date.today(),
                },
            ],
        ]

    def location(self, obj):
        if isinstance(obj, dict):
            return obj["location"]
        elif isinstance(obj, Category):
            return reverse(
                "ai_pictures:ai-porn-videos-category", kwargs={"category": obj.slug}
            )
        elif isinstance(obj, Website):
            return reverse(
                "ai_pictures:ai-porn-videos-source", kwargs={"source": obj.slug}
            )
        else:
            return super().location(obj)
