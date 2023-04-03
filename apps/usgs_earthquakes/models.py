from django.db import models
from apps.cities import models as m_cities

# Create your models here.

from django.db import models

class Earthquake(models.Model):
    magnitude = models.FloatField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField()

class SearchResult(models.Model):
    city = models.ForeignKey(m_cities.City, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    nearest_earthquake = models.ForeignKey(Earthquake, on_delete=models.CASCADE, null=True)
    

