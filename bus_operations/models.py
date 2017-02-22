from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BusRoutes(models.Model):
	name = models.CharField(max_length=100)

class Bus(models.Model):
	number_plate = models.CharField(max_length=7)
	passenger_seats = models.IntegerField()
		
