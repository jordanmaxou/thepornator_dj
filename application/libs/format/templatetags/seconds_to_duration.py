import time

from django import template

register = template.Library()


@register.filter(name="seconds_to_duration")
def seconds_to_duration(value):
    value = int(value)
    return time.strftime(
        "%H:%M:%S" if value > 3600 else "%M:%S", time.gmtime(int(value))
    )
