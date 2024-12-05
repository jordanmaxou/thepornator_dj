import requests
import json

from django.conf import settings


def get_client_ip(request):
    if settings.DEBUG:
        response = requests.get("https://api.ipify.org?format=json")
        if (
            response.ok
            and (data := json.loads(response.content))
            and (ip := data.get("ip"))
        ):
            return ip
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
