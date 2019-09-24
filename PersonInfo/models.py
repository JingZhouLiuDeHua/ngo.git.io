from django.db import models

# Create your models here.
class PersonInfo(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)