from django.shortcuts import render
from frontend import utils as u_frontend
import requests
from requests.auth import HTTPBasicAuth

def landing_page(request):
    
    return render(request, 'frontend/index.html', {})


def add_city(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        
        u_frontend.add_city(city)
        
        return render(request, 'frontend/index.html', {})
    else:
        return render(request, 'frontend/index.html', {})