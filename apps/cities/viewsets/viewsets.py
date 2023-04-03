from rest_framework import viewsets
from apps.cities import models as m_cities
from apps.cities.serializers import serializers as sz_cities

from geopy.geocoders import Nominatim

class CityViewSet(viewsets.ModelViewSet):
    queryset = m_cities.City.objects.all()
    serializer_class = sz_cities.CitySerializer
    
    