from rest_framework import viewsets, status
from apps.usgs_earthquakes import models as m_usgs_earthquakes
from apps.usgs_earthquakes import utils as u_usgs_earthquakes
from apps.cities import models as m_cities
from apps.cities import utils as u_cities
from apps.logs import utils as u_logs


from apps.usgs_earthquakes.serializers import serializers as sz_usgs_earthquakes
from rest_framework.response import Response


class EarthquakeViewSet(viewsets.ModelViewSet):
    queryset = m_usgs_earthquakes.Earthquake.objects
    serializer_class = sz_usgs_earthquakes.EarthquakeSerializer
    error_message = {'error':'verify the link composition and try again'}
    
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def list(self, request):
        try:
            min_magnitude = request.query_params.get('min_magnitude') or request.data.get('min_magnitude', '5.1')
            start_date = request.query_params.get('start_date') or request.data.get('start_date')
            end_date = request.query_params.get('end_date') or request.data.get('end_date')
            
            if(start_date and end_date):
                if m_usgs_earthquakes.SearchResult.objects.filter(start_date=start_date, end_date=end_date).exists():
                    queryset_eartquakes = self.queryset.filter(date__gte=start_date, date__lte=end_date).order_by('date')

                else:
                    eartquakes = u_usgs_earthquakes.get_earthquakes(start_date, end_date, min_magnitude)
                
                    u_usgs_earthquakes.save_earthquakes(eartquakes)
                    
                    
                    queryset_eartquakes = self.queryset.filter(date__gte=start_date, date__lte=end_date)

                    m_usgs_earthquakes.SearchResult.objects.create(start_date=start_date, end_date=end_date)
            else:
                queryset_eartquakes = self.queryset.order_by('date')

            queryset = queryset_eartquakes.all()

            serializer = self.serializer_class(queryset,  many=True)
            
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
            

class SearchResultViewSet(viewsets.ModelViewSet):
    queryset = m_usgs_earthquakes.SearchResult.objects
    serializer_class = sz_usgs_earthquakes.SearchResultSerializer
    error_message = {'error':'verify the link composition and try again'}
    
    def list(self, request):
        try:
            city = request.query_params.get('city') or request.data.get('city')
            start_date = request.query_params.get('start_date') or request.data.get('start_date')
            end_date = request.query_params.get('end_date') or request.data.get('end_date')
            min_magnitude = request.query_params.get('min_magnitude') or request.data.get('min_magnitude', '5.1')
            
            
            if  m_cities.City.objects.filter(name=city).exists():
                actual_city = m_cities.City.objects.get(name=city)
                
                if self.queryset.filter(start_date=start_date, end_date=end_date, city=actual_city).exists():      
                    queryset_searchs = self.queryset.filter(start_date=start_date, end_date=end_date, city=actual_city).all()

                else:
                    if self.queryset.filter(start_date=start_date, end_date=end_date).exists():
                        queryset_eartquakes = m_usgs_earthquakes.Earthquake.objects.filter(date__gte=start_date, date__lte=end_date)
                                
                    else:
                        eartquakes = u_usgs_earthquakes.get_earthquakes(start_date, end_date, min_magnitude)
                        u_usgs_earthquakes.save_earthquakes(eartquakes)
                        queryset_eartquakes = m_usgs_earthquakes.Earthquake.objects.filter(date__gte=start_date, date__lte=end_date)
                        
                    coordinates = [actual_city.latitude, actual_city.longitude]
                    
                    nearest_earthquake = u_cities.get_distance(coordinates[0], coordinates[1], queryset_eartquakes)
                    
                    self.queryset.create(start_date=start_date, end_date=end_date, city=actual_city, nearest_earthquake=nearest_earthquake[0], distance_km=nearest_earthquake[1])
                    
                    queryset_searchs = self.queryset.filter(start_date=start_date, end_date=end_date, city=actual_city).all()
                    
            else:
                queryset_searchs = self.queryset.all().order_by('-id')
                
            queryset = queryset_searchs

            serializer = self.serializer_class(queryset,  many=True)
            return Response(serializer.data)
        
        except Exception as e:
            u_logs.create_log(e)
            return Response(self.error_message)