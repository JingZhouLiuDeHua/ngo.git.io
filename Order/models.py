from django.db import models

# Create your models here.
class Order(models.Model):
    DonationType = models.CharField(max_length=50)
    Quality = models.PositiveIntegerField()
    Amount = models.PositiveIntegerField()
    TotalAmount = models.PositiveIntegerField()