# encoding: utf-8
from rest_framework import viewsets
from serializers import *

class ParkingViewSet(viewsets.ModelViewSet):
    """
        Se obtiene la información del Auto de acuerdo a la patente
        http://localhost:8000/api-parking/?patent={patent}
    """
    serializer_class = ParkingSerializer

    def get_queryset(self):
        queryset = Parking.objects.all()
        patent = self.request.query_params.get("patent", None)
        if patent is not None:
            queryset = queryset.filter(car__patent=patent)
        return queryset
