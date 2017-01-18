# encoding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from models import *
from forms import *


def driver_new(request):
    if request.method == "POST":
        form = DriverForm(request.POST or None)
        if form.is_valid():
            driver = form.save(commit=False)
            driver = form.save()
            return redirect('car_new', pk_driver=driver.id)
    else:
        form = DriverForm()
    driver = Driver.objects.all().order_by('-id')
    template = "driver_new.html"
    context = {'form': form, 'driver': driver}
    return render(request, template, context)


def car_new(request, pk_driver):
    if request.method == "POST":
        form = CarForm(request.POST or None)
        if form.is_valid():
            car = form.save(commit=False)
            car.driver = Driver.objects.get(id=pk_driver)
            car = form.save()
            return redirect('car_new', pk_driver=pk_driver)
    else:
        form = CarForm()
    car = Car.objects.filter(driver_id=pk_driver).order_by('-id')
    template = "car_new.html"
    context = {'form': form, 'car': car}
    return render(request, template, context)


def parking_new(request, pk_car):
    if request.method == "POST":
        form = ParkingForm(request.POST or None)
        if form.is_valid():
            parking = form.save(commit=False)
            parking.car = Car.objects.get(pk=pk_car)
            car = form.save()
            return redirect('parking_days')
    else:
        form = ParkingForm()
    template = "parking_new.html"
    context = {'form': form}
    return render(request, template, context)


def parking_days(request):
    if request.method == "POST":
        patent = request.POST['patent']
        parking = get_object_or_404(Parking, car__patent=patent)
        days_parking = parking.days_in_parking()
    else:
        patent = ''
        days_parking = ''
    template = "search_patent.html"
    context = {'days_parking': days_parking, 'patent': patent}
    return render(request, template, context)
