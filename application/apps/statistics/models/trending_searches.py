from django.db import models


class TrendingSearches(models.Model):
    request = models.CharField(max_length=255)
    date = models.DateField()
    nb_result = models.PositiveIntegerField()
    lang = models.CharField(max_length=10)
