from modeltranslation.translator import register, TranslationOptions
from apps.websites.models import Website, Category


@register(Website)
class WebsiteTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description")
