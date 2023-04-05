from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.usgs_earthquakes.viewsets import viewsets as v_usgs_earthquakes
from apps.cities.viewsets import viewsets as v_cities
from frontend import urls as u_frontend



route = routers.DefaultRouter()
route.register(r'cities', v_cities.CityViewSet, basename='cities')
route.register(r'earthquakes', v_usgs_earthquakes.EarthquakeViewSet, basename='earthquakes')
route.register(r'nearest-earthquake', v_usgs_earthquakes.SearchResultViewSet, basename='nearest-earthquakes')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include(route.urls)),
    path('', include(u_frontend)),
]
