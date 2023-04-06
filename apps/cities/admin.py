from django.contrib import admin
from apps.cities import models as m_cities

admin.site.register(m_cities.City)