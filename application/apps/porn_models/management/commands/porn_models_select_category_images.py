from django.core.management.base import BaseCommand

from apps.porn_models.models import Profile, Category, TypeOfStatus


class Command(BaseCommand):
    help = "Upgrade main images for all categories"

    def handle(self, *_args, **_kwargs):
        excluded_ids = []
        for category in Category.objects.all():
            selected = (
                Profile.objects.filter(
                    status=TypeOfStatus.OK,
                    categories=category,
                )
                .exclude(id__in=excluded_ids)
                .first()
            )
            if selected is not None:
                excluded_ids.append(selected.id)
            category.main_profile = selected
            category.save(update_fields=["main_profile"])
