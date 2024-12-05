from django.utils.translation import get_language

from apps.ads.models import TopLink


def top_link(request):
    return {
        "top_links": (
            TopLink.objects.filter(lang=get_language(), enabled=True)
            .order_by("position")
            .values("label", "link")
        )
    }
