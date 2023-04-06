from django.contrib import admin
from apps.usgs_earthquakes import models as m_usgs_earthquakes

class EarthquakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'magnitude', 'location', 'latitude', 'longitude', 'date')
    list_filter = ('location', 'magnitude')
    search_fields = ('location',)

class SearchResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'start_date', 'end_date', 'nearest_earthquake','distance_km')
    list_filter = ('city',)
    search_fields = ('city',)

admin.site.register(m_usgs_earthquakes.Earthquake, EarthquakeAdmin)
admin.site.register(m_usgs_earthquakes.SearchResult, SearchResultAdmin)