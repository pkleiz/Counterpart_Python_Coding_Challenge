from rest_framework import serializers
from apps.usgs_earthquakes import models as m_usgs_earthquakes

class EarthquakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_usgs_earthquakes.Earthquake
        fields = '__all__'

class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_usgs_earthquakes.SearchResult
        fields = '__all__'