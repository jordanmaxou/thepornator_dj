from modeltranslation.translator import register, TranslationOptions
from .models import Category, Video, Channel


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Channel)
class ChannelTranslationOptions(TranslationOptions):
    fields = ("description",)
