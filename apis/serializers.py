from django.contrib.auth.models import *
from rest_framework import serializers
from parkings.models import *

class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = ('id','url','days','days_in_parking')
