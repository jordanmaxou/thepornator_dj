from datetime import date

from django.core.management.base import BaseCommand

from apps.ai_pictures.models import Content, Category, TypeOfStatus, TypeOfContent


class Command(BaseCommand):
    help = "Upgrade main images picture and images video fo all categories"

    def handle(self, *_args, **_kwargs):
        excluded_ids = []
        for category in Category.objects.all():
            selected = (
                Content.objects.filter(
                    status=TypeOfStatus.OK,
                    publication_date__lte=date.today(),
                    type=TypeOfContent.IMAGE,
                    categories=category,
                )
                .exclude(id__in=excluded_ids)
                .order_by("-publication_date")
                .first()
            )
            if selected is not None:
                excluded_ids.append(selected.id)
            category.main_image_content = selected
            category.save(update_fields=["main_image_content"])

            selected = (
                Content.objects.filter(
                    status=TypeOfStatus.OK,
                    publication_date__lte=date.today(),
                    type=TypeOfContent.VIDEO,
                    categories=category,
                )
                .exclude(id__in=excluded_ids)
                .order_by("-publication_date")
                .first()
            )
            if selected is not None:
                excluded_ids.append(selected.id)
            category.main_video_content = selected
            category.save(update_fields=["main_video_content"])
