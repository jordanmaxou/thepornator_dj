from modeltranslation.translator import register, TranslationOptions
from .models import Category, Content, Country


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ("title",)
