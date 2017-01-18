# encoding: utf-8

from django.test import TestCase
from models import *
from datetime import date, datetime, timedelta

class DriverTest(TestCase):

    def test_driver_creation(self):
        driver = Driver(rut = "123456781", name="Jimi", lastname="Hendrix", sex="M", age=24)
        driver.save()

    def test_car_creation(self):
        driver = Driver(rut = "123456782", name="Sherlock", lastname="Holmes", sex="M", age=34)
        driver.save()

        car = Car(driver = driver, brand="Mercedes Benz", color="Negro", patent="XX-XX-XX", chassis="tílde")
        car.save()

        parking = Parking(car = car, days=27, number=7)
        parking.save()

    def test_parking_creation(self):
        driver = Driver(rut = "123456783", name="Kvothe", lastname="Kvothe", sex="M", age=34)
        driver.save()

        car = Car(driver = driver, brand="Tesla", color="Negro", patent="XX-XX-XX", chassis="tílde")
        car.save()

        parking = Parking(car = car, days=27, number=7)
        parking.save()

    def test_parking_day(self):
        """ Return a days
            Se simula la fecha actual adelantada en 20 días y se calculan los días aparcados,
            se espera el resultado 20 (días)
        """
        today_future = date.today() + timedelta(20)
        date_parking = date.today()
        days = today_future - date_parking
        self.assertEquals(days.days, 20, True)
