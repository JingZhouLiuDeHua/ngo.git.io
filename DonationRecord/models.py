from django.db import models

# Create your models here.
class DonationRecord(models.Model):
    Name = models.CharField(max_length=50)
    Date = models.DateTimeField(auto_now_add=True)
    Amount = models.PositiveIntegerField()
    DonationType  =   models.CharField(max_length=250)