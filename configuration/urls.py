from django.contrib import admin
from django.urls import path, include
from apps.cities import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
]
