from django.db import models
from django.contrib.auth.models import User
# from exchange.models import Exchange

class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    symbol = models.CharField(max_length=10, default='', blank=False, null=True)
    name = models.CharField(max_length=255, default='', blank=False, null=True)
    marketCap = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)
    exchange = models.CharField(max_length=10, default='', blank=False, null=True)
    postMarketChangePercent = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)
    regularMarketPrice = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)
    regularMarketChangePercent = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)

    def __str__(self):
        return self.symbol + " - "+ self.name