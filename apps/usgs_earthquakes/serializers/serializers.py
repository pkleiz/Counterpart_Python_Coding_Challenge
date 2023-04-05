from rest_framework import serializers
from apps.usgs_earthquakes import models as m_usgs_earthquakes

class EarthquakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_usgs_earthquakes.Earthquake
        fields = '__all__'

class SearchResultSerializer(serializers.ModelSerializer):
    
    city = serializers.CharField(source='city.name', allow_null=True, default='search without defined location')
    nearest_earthquake = serializers.CharField(source='nearest_earthquake.title', allow_null=True, default='')
    nearest_earthquake_date = serializers.CharField(source='nearest_earthquake.date', allow_null=True, default='')

    class Meta:
        model = m_usgs_earthquakes.SearchResult
        fields = '__all__'