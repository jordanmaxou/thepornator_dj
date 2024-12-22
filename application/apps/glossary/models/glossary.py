from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from .count import Count
from apps.glossary.utils import enrich_text_with_glossary_link


class TypeOfTerm(models.TextChoices):
    POSITION = "position", _("Position")
    ACRONYM = "acronym", _("Acronym")
    VOCABULARY = "vocabulary", _("Vocabulary")


class Languages(models.TextChoices):
    FR = "fr"
    EN = "en"


class Glossary(models.Model):
    class Meta:
        verbose_name_plural = "glossaries"

    slug = models.SlugField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TypeOfTerm)
    meaning = models.TextField(max_length=100, null=True)
    definition = models.TextField(max_length=1200)
    picture = models.FileField(upload_to="img/glossary", null=True, blank=True)
    publication_date = models.DateField()
    lang = models.CharField(max_length=2, choices=Languages, null=True)
    count = models.OneToOneField(Count, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.definition_en:
            self.definition_en = enrich_text_with_glossary_link(
                self.__class__.objects.exclude(id=self.id)
                .filter(**({"lang": self.lang}) if self.lang else None)
                .values_list("slug", flat=True),
                self.definition_en,
            )
        if self.definition_fr:
            self.definition_fr = enrich_text_with_glossary_link(
                self.__class__.objects.exclude(id=self.id)
                .filter(**({"lang": self.lang}) if self.lang else None)
                .values_list("slug", flat=True),
                self.definition_fr,
            )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("glossary:content", kwargs={"term": self.slug})

    def up(self):
        Count.objects.filter(id=self.count.id).update(up=models.F("up") + 1)

    def down(self):
        Count.objects.filter(id=self.count.id).update(up=models.F("down") + 1)

    def __str__(self):
        return f"{self.slug} ({self.name})"
