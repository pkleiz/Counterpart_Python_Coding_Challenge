from django.urls import path
from frontend import views as v_frontend


urlpatterns = [
    path('', v_frontend.landing_page, name="home"),
    path('add-city/', v_frontend.add_city, name="add-city"),
]
