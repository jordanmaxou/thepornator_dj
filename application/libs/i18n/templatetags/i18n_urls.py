from django import template
from django.urls import translate_url

register = template.Library()


@register.simple_tag(takes_context=True)
def path_with_lang(context, lang: str):
    path = context["request"].path

    return translate_url(path, lang)
