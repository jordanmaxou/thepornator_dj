from modeltranslation.translator import register, TranslationOptions
from .models import Question, Theme


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ("sentence",)


@register(Theme)
class ThemeTranslationOptions(TranslationOptions):
    fields = ("name",)
