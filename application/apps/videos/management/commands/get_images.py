from django.core.management.base import BaseCommand
from apps.videos.models import Video


class Command(BaseCommand):
    help = "Allow to download and save images from ai_pictures with no image yet"

    def handle(self, *_args, **_kwargs):
        selected_contents = Video.objects.filter(status__isnull=True)
        for selected_content in selected_contents:
            selected_content.retrieve_image()
