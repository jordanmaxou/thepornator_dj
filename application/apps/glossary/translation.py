from modeltranslation.translator import register, TranslationOptions
from .models import Glossary


@register(Glossary)
class GlossaryTranslationOptions(TranslationOptions):
    fields = ("name", "definition")
