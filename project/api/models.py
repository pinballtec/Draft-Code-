from django.db import models

# Create your models here.

usd_eu_y = (
        ('DOLLARS', 'USD'),
        ('EURO', 'EU'),
        ('STERLING', 'GBR'),
        ('ZLOTY', 'PLN')
    )


class Paybylink(models.Model):
    created_at = models.TimeField(auto_now_add=True, blank=True)
    currency = models.CharField(max_length=10, choices=usd_eu_y)
    amount = models.IntegerField()
    description = models.CharField(max_length=200)
    bank = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Dp(models.Model):
    link = models.ManyToManyField(Paybylink, blank=True)
    created_at = models.TimeField(auto_now_add=True, blank=True)
    currency = models.CharField(max_length=10,choices=usd_eu_y)
    amount = models.IntegerField()
    description = models.CharField(max_length=200)
    iban = models.CharField(max_length=100)

    def __str__(self):
        return self.iban


class Card(models.Model):
    link = models.ManyToManyField(Paybylink, blank=True)
    created_at = models.TimeField(auto_now_add=True, blank=True, unique=True)
    currency = models.CharField(max_length=10, choices=usd_eu_y)
    amount = models.IntegerField()
    description = models.CharField(max_length=200)
    cardholder_name = models.CharField(max_length=20)
    cardholder_surname = models.CharField(max_length=20)
    card_number = models.IntegerField()

    def __str__(self):
        return self.cardholder_name