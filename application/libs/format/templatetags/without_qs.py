from django import template
from urllib.parse import urlparse, urlunparse

register = template.Library()


@register.filter(name="without_qs")
def without_qs(value):
    parsed_url = urlparse(value)
    return urlunparse(parsed_url._replace(query=""))
