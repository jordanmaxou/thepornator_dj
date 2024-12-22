from django.db import models

from .type_deal import TypeDeal
from .payment_method import PaymentMethod


class Deal(models.Model):
    class StatusOfDeal(models.TextChoices):
        RUNNING = "Running"
        WAITING = "Waiting"
        CANCELLED = "Cancelled"

    contact = models.CharField(max_length=100)
    status = models.SlugField(max_length=50, choices=StatusOfDeal)
    program = models.URLField(max_length=200)
    type = models.ManyToManyField(TypeDeal)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    amount_available = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.SET_NULL, null=True
    )
    potential = models.SmallIntegerField(default=0)
    comment = models.TextField(max_length=500, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return self.contact
