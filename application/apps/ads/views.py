from django.conf import settings
from django.http import JsonResponse
from django.views.generic.base import View
from django.db.models import CharField, Value, F
from django.db.models.functions import Concat
from django.utils.translation import get_language

from apps.ads.models import Banner


class BannerListView(View):
    def get(self, _request):
        return JsonResponse(
            {
                "banners": list(
                    Banner.objects.filter(
                        languages__contains=[get_language()], enabled=True
                    )
                    .annotate(
                        image_path=Concat(
                            Value(settings.MEDIA_URL),
                            F("image"),
                            output_field=CharField(),
                        )
                    )
                    .values()
                )
            }
        )
