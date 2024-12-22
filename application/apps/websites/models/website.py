from urllib.parse import urlparse, urlunparse

from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from .category import Category
from .deal import Deal


class WebsiteManager(models.Manager):
    def by_category_avg_notes(self):
        return (
            self.annotate(
                avg_note_update=models.Avg("questionwebsite__note_update"),
                has_running_deal=models.Case(
                    models.When(
                        deal__status=Deal.StatusOfDeal.RUNNING, then=models.Value(True)
                    ),
                    default=models.Value(False),
                    output_field=models.BooleanField(),
                ),
            )
            .select_related("category")
            .order_by("category__position", "-avg_note_update")
        )

    def get_notes_by_websites(self):
        queryset = self.annotate(
            note=models.Case(
                models.When(
                    questionwebsite__note_update__isnull=False,
                    then=models.F("questionwebsite__note_update"),
                ),
                default=models.F("questionwebsite__note_init"),
            )
        ).values("questionwebsite__website_id", "questionwebsite__question_id", "note")

        result = {}
        for item in queryset:
            website_id = item["questionwebsite__website_id"]
            question_id = item["questionwebsite__question_id"]
            note = item["note"]

            if website_id not in result:
                result[website_id] = {}
            result[website_id][question_id] = note

        return result


class Website(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=250)
    icon = models.FileField(max_length=150, upload_to="img/logosites")
    screen = models.FileField(max_length=150, upload_to="img/screensites")
    is_direct_link = models.BooleanField()
    description = models.TextField(max_length=10000)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True, blank=True)
    click = models.PositiveBigIntegerField(default=0)
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, null=True, blank=True)
    questions = models.ManyToManyField(
        "surveys.Question",
        through="surveys.QuestionWebsite",
        through_fields=("website", "question"),
    )

    objects = WebsiteManager()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.replace(".", ""))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("websites:site", kwargs={"website": self.slug})

    @property
    def base_website_url(self) -> str:
        url_parsed = urlparse(self.url)
        return urlunparse((url_parsed.scheme, url_parsed.netloc, "", "", "", ""))

    @property
    def website_host(self) -> str:
        url_parsed = urlparse(self.url)
        return url_parsed.hostname

    @property
    def avg_notes_by_theme(self) -> dict:
        return {
            item["question__theme__name"]: round(item["avg_note_update"], 2)
            for item in (
                self.questions.through.objects.prefetch_related(
                    "question", "question__theme"
                )
                .filter(website_id=self.id)
                .values("question__theme__name")
                .annotate(avg_note_update=models.Avg("note_update"))
            )
        }

    @property
    def avg_note(self) -> float:
        return round(
            self.questions.through.objects.filter(website_id=self.id).aggregate(
                models.Avg("note_update")
            )["note_update__avg"],
            4,
        )

    @property
    def reviews(self) -> int:
        return self.podium_set.filter(first=self, survey__is_valid=True).count()

    def update_counter(self):
        self.__class__.objects.filter(id=self.id).update(click=models.F("click") + 1)
