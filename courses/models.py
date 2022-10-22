from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, null=True)
    symbol = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.symbol


class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    price = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
