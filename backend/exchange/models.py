from django.db import models

class Currency(models.TextChoices):
    CAD = 'CAD'
    USD = 'USD'

class Country(models.TextChoices):
    CANADA = 'CANADA'
    USA = 'USA'

class Exchange(models.Model):
    exchangeID = models.CharField(max_length=255, default="", blank=False)
    exchangeName = models.CharField(max_length=255, default="", blank=False)
    currency = models.CharField(max_length=30, choices=Currency.choices)
    country = models.CharField(max_length=30, choices=Country.choices)