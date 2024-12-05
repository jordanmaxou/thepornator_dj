import json

from django.core.serializers.json import DjangoJSONEncoder
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.template import Library

_json_script_escapes = {
    ord(">"): "\\u003E",
    ord("<"): "\\u003C",
    ord("&"): "\\u0026",
}

register = Library()


@register.filter(is_safe=True)
def json_ld_script(value):
    json_str = json.dumps(value, cls=DjangoJSONEncoder).translate(_json_script_escapes)
    template = '<script type="application/ld+json">{}</script>'
    args = (mark_safe(json_str),)
    return format_html(template, *args)
