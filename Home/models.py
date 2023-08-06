from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=100)
    return_rate = models.DecimalField(max_digits=5, decimal_places=2)
    risk_level = models.PositiveIntegerField()

class MutualFund(models.Model):
    name = models.CharField(max_length=100)
    return_rate = models.DecimalField(max_digits=5, decimal_places=2)
    risk_level = models.PositiveIntegerField()