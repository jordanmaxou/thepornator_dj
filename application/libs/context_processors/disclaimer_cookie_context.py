from django.conf import settings


def disclaimer_cookie_context(request):
    return {
        "has_disclaimer_cookie": request.COOKIES.get(settings.DISCLAIMER_COOKIE_NAME)
        is True
    }
