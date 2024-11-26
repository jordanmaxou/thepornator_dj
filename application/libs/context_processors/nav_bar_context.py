from django.urls import reverse
from apps.websites.models import Category
from apps.porn_models.models import Website


def nav_bar_context(request):
    return {
        "website_categories": [
            {
                "name": cat.name,
                "slug": cat.slug,
                "url": reverse("websites:category", kwargs={"category": cat.slug}),
                "icon": cat.icon.url,
            }
            for cat in Category.objects.all()
            .only("slug", "name", "icon")
            .order_by("position")
        ],
        "performer_websites": [
            {"name": website.name, "slug": website.slug}
            for website in Website.objects.only("slug", "name").all()
        ],
    }
