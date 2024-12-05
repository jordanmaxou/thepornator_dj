from django.conf import settings
from django.urls import translate_url


def alternates(request):
    return {
        "alternates": {
            "x-default": request.build_absolute_uri(
                translate_url(request.path, settings.LANGUAGE_CODE)
            ),
            **{
                language_code: request.build_absolute_uri(
                    translate_url(request.path, language_code)
                )
                for language_code, _ in settings.LANGUAGES
            },
        }
    }
