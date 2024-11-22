from django import template

register = template.Library()


def str_word_count(test):
    tab = test.split(" ")
    return len(tab)


@register.filter(name="estimate_reading_duration")
def estimate_reading_duration(value, reading_speed=250):
    word_count = str_word_count(value)
    durationMinutes = round(word_count / reading_speed)

    return durationMinutes
