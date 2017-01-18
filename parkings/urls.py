from django.conf.urls import url
from parkings import views

urlpatterns = [
    url(r'^$', views.driver_new, name="driver_new"),
    url(r'^new_car/(?P<pk_driver>[0-9]+)/$', views.car_new, name="car_new"),
    url(r'^new_parking/(?P<pk_car>[0-9]+)/$', views.parking_new, name="parking_new"),
    url(r'^days/$', views.parking_days, name="parking_days"),
]
