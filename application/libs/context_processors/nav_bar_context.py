from django.urls import reverse
from apps.websites.models import Category


def nav_bar_context(request):
    return {
        "website_categories": [
            {
                "name": cat.name,
                "url": reverse("websites:category", kwargs={"category": cat.slug}),
                "icon": cat.icon.url,
            }
            for cat in Category.objects.all()
            .only("slug", "name", "icon")
            .order_by("position")
        ]
    }
