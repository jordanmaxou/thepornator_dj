from typing import Iterable

from django.urls import reverse


def get_link(label, slug):
    return f"""<a style="color:#009961; text-decoration: none; font-weight:bold;" href="{reverse('glossary:content', kwargs={'term': slug})}">{label}</a>"""


def enrich_text_with_glossary_link(
    all_glossary_slugs: Iterable["str"], text: str
) -> str:
    words = text.split(" ")
    # print(words)
    for i, word in enumerate(words):
        slug = word.strip().lower()
        if slug in all_glossary_slugs:
            words[i] = get_link(word, slug)
    return " ".join(words)
