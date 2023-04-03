from rest_framework import viewsets, status
from apps.usgs_earthquakes import models as m_usgs_earthquakes
from apps.cities import models as m_cities
from apps.usgs_earthquakes.serializers import serializers as sz_usgs_earthquakes
from rest_framework.response import Response
from apps.logs import utils as u_logs


class EarthquakeViewSet(viewsets.ModelViewSet):
    queryset = m_usgs_earthquakes.Earthquake.objects
    serializer_class = sz_usgs_earthquakes.EarthquakeSerializer
    
    def create(self, request):
        try:
            city = m_cities.City.objects.get(name=request.data.get('name',''))
            
            start_date = request.data.get('start_date')
            end_date = request.data.get('end_date')
            
            city = self.queryset.create(
                name=request.data.get('name'),
                latitude=request.data.get('latitude'),
                longitude=request.data.get('longitude')
            )
            
            serializer = self.serializer_class(city)
            return Response(serializer.data)
        
        except Exception as e:
            u_logs.create_log(e)

    
    def list(self, request):
        try:
            queryset = self.queryset.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            u_logs.create_log(e)
    
    def delete(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            u_logs.create_log(e)