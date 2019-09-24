from django.db import models

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.CharField(max_length=250)
    Password  = models.CharField(max_length=250)
    Role = models.CharField(max_length=250)