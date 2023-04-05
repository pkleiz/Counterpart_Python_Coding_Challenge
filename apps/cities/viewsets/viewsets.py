from rest_framework import viewsets, status
from apps.cities import models as m_cities
from apps.cities import utils as u_cities
from apps.cities.serializers import serializers as sz_cities
from rest_framework.response import Response
from apps.logs import utils as u_logs


class CityViewSet(viewsets.ModelViewSet):
    queryset = m_cities.City.objects
    serializer_class = sz_cities.CitySerializer
    error_message = {'error':'verify the link composition and try again'}
    
    
    def create(self, request):
        try:
            name = request.query_params.get('name') or request.data.get('name')
            latitude = request.query_params.get('latitude') or request.data.get('latitude')
            longitude = request.query_params.get('longitude') or request.data.get('longitude')
            
            if (not latitude or longitude):
                lat_long = u_cities.get_lat_long(name)
                latitude = lat_long[0]
                longitude = lat_long[1]
                if(len(lat_long) == 3):
                    description = lat_long[2]
                    return Response({'error':description})
                
            city = self.queryset.create(
                name = name,
                latitude = latitude,
                longitude = longitude,
            )

            serializer = self.serializer_class(city)
            return Response(serializer.data)
        
        except Exception as e:
            u_logs.create_log(e)
            return Response(self.error_message)

    
    def list(self, request):
        try:
            queryset = self.queryset.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            u_logs.create_log(e)
            return Response(self.error_message)
            
    
    def delete(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            u_logs.create_log(e)
            return Response(self.error_message)