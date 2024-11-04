from modeltranslation.translator import register, TranslationOptions
from .models import Story, Tag


@register(Story)
class StoryTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)
