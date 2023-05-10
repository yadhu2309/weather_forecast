from django.db import models

# Create your models here.

class Weather(models.Model):
    city = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    temp = models.IntegerField()
    condition = models.TextField()
