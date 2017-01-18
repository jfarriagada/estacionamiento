# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import date

SEX_CHOICES = (
    ("M","Masculino"),
    ("F","Femenino")
)

class Driver(models.Model):
    created = models.DateField(auto_now_add=True)
    rut = models.CharField(max_length=12, unique=True, null=False, blank=False)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    sex = models.CharField(choices=SEX_CHOICES, default="M", max_length=1)
    age = models.IntegerField()

class Car(models.Model):
    created = models.DateField(auto_now_add=True)
    driver = models.ForeignKey(Driver)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    patent = models.CharField(max_length=10, unique=True, null=False, blank=False)
    chassis = models.CharField(max_length=20)

class Parking(models.Model):
    created = models.DateField(auto_now_add=True)
    car = models.ForeignKey(Car)
    days = models.IntegerField(null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)

    def days_in_parking(self):
        """ Return a days
            se obtiene la cantidad de días que lleva aparcado el Auto
        """
        today = date.today()
        date_parking = self.created
        days = today - date_parking
        return days.days