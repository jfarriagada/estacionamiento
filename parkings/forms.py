# -*- encoding: utf-8 -*-
from django import forms
from parkings.models import *


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            "rut": forms.TextInput(attrs={"class": "form-control", "placeholder": "Solo numeros"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lastname": forms.TextInput(attrs={"class": "form-control"}),
            "sex": forms.Select(choices=SEX_CHOICES, attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"})
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('driver',)
        widgets = {
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(attrs={"class": "form-control"}),
            "patent": forms.TextInput(attrs={"class": "form-control"}),
            "chassis": forms.TextInput(attrs={"class": "form-control"})
        }


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        exclude = ('car',)
        widgets = {
            "days": forms.NumberInput(attrs={"class": "form-control"}),
            "number": forms.NumberInput(attrs={"class": "form-control"})
        }
