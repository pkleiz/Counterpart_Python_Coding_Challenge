from rest_framework import viewsets, status
from apps.cities import models as m_cities
from apps.cities.serializers import serializers as sz_cities
from rest_framework.response import Response


class CityViewSet(viewsets.ModelViewSet):
    queryset = m_cities.City.objects
    serializer_class = sz_cities.CitySerializer
    
    def create(self, request):
        
        city = self.queryset.create(
            name=request.data.get('name'),
            latitude=request.data.get('latitude'),
            longitude=request.data.get('longitude')
        )
        
        serializer = self.serializer_class(city)
        return Response(serializer.data)
    
    def list(self, request):
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)