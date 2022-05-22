from django.db import models

# Create your models here.


class Paybylink(models.Model):
    created_at = models.TimeField(auto_now_add=True, blank=True)
    currency = models.CharField(max_length=10)
    amount = models.IntegerField(max_length=2000000000)
    description = models.CharField(max_length=200)
    bank = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Dp(models.Model):
    link = models.ForeignKey(Paybylink, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True, blank=True)
    currency = models.CharField(max_length=10)
    amount = models.IntegerField(max_length=2000000000)
    description = models.CharField(max_length=200)
    iban = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Card(models.Model):
    link = models.ForeignKey(Paybylink, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True, blank=True)
    currency = models.CharField(max_length=10)
    amount = models.IntegerField(max_length=2000000000)
    description = models.CharField(max_length=200)
    cardholder_name = models.CharField(max_length=20)
    cardholder_surname = models.CharField(max_length=20)
    card_number = models.IntegerField(max_length=16)

    def __str__(self):
        return self.cardholder_name