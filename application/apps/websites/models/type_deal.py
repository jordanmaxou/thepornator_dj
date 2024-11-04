from django.db import models


class TypeDeal(models.Model):
    name = models.CharField(max_length=50)
