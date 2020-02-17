from django.db import models
from configparser import ConfigParser
from djongo import models

config = ConfigParser()
config.read('config.ini')
db = config['mongodb']


# Create your models here.
class SellerListings(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=15, decimal_places=7)
    latitude = models.DecimalField(max_digits=15, decimal_places=7)
    amount = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name

