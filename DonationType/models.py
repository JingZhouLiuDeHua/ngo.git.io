from django.db import models

# Create your models here.
class DonationType(models.Model):
    Name = models.CharField(max_length=50)
    RecurringGift = models.PositiveIntegerField()  #1 yes 0 no