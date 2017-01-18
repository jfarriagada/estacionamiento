from django.conf.urls import url, include
from rest_framework import routers
from apis import views

router = routers.DefaultRouter()
router.register(r'parking', views.ParkingViewSet, base_name='parking')
router.register(r'parking', views.ParkingViewSet, base_name='parking-detail')

urlpatterns = [
    url(r'^api-', include(router.urls)),
]
