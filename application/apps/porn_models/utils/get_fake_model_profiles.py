import logging
import json

from django.conf import settings
from django.apps import apps

import requests

logger = logging.getLogger(__name__)


def get_websites():
    Website = apps.get_model("porn_models", "website")
    return {website.slug: website for website in Website.objects.all()}


def get_fake_model_profiles(website_slug):
    websites = get_websites()
    raw_results = get_json_from_url(website_slug)
    results = []
    for raw_result in raw_results:
        results.append(
            {
                "id": 0,
                "slug": raw_result["username"],
                "pseudo": raw_result["displayName"],
                "local_photo": {"url": raw_result["avatar"]},
                "description": raw_result["about"],
                "counts": {
                    "likes": int(raw_result["favoriteCount"]),
                    "photos": 0,
                    "videos": 0,
                    "posts": 0,
                },
                "price": "Free"
                if raw_result["subscribePrice"] == "0"
                else f"${int(raw_result['subscribePrice'])/100}",
                "website": websites.get(website_slug),
                "ads": True,
                "url": raw_result["refUrl"],
            }
        )

    return results


def get_json_from_url(website_slug):
    url = settings.SOCIAL_PROFILE_URL + f"&ref=https://thepornator.com/{website_slug}"
    response = requests.get(
        url, headers={"Authorization": f"Bearer {settings.SOCIAL_PROFILE_BEARER}"}
    )
    if response.ok:
        data = json.loads(response.content)
        if data and (results := data.get("results")):
            return results
    logger.error(
        f"An error occurs during fake model profile retrieval. Status {response.status_code}"
    )
    return []
