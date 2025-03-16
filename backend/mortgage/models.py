from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class MortgageOffer(models.Model):
    bank_name = models.CharField(
        verbose_name="Bank Name",
        max_length=10
    )
    term_min = models.PositiveIntegerField(
        verbose_name="Mortgage Term, FROM"
    )
    term_max = models.PositiveIntegerField(
        verbose_name="Mortgage Term, TO"
    )
    rate_min = models.FloatField(
        verbose_name="Interest Rate, FROM"
    )
    rate_max = models.FloatField(
        verbose_name="Interest Rate, TO"
    )
    payment_min = models.PositiveIntegerField(
        verbose_name="Loan Amount, FROM"
    )
    payment_max = models.PositiveIntegerField(
        verbose_name="Loan Amount, TO"
    )

    class Meta:
        verbose_name = "Mortgage Offer"
        verbose_name_plural = "Mortgage Offers"

    def __str__(self):
        return self.bank_name
