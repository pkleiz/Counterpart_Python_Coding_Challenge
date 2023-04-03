from django.urls import path, include
from rest_framework import routers
from apps.cities.viewsets import viewsets as v_cities

route = routers.DefaultRouter()
route.register(r'add_city', v_cities.CityViewSet, basename='Add a city')

urlpatterns = [
    path('', include(route.urls)),
]
