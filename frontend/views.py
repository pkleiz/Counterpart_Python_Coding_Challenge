from django.shortcuts import render
from frontend import utils as u_frontend

def landing_page(request):
    
    return render(request, 'frontend/index.html', {})


def add_city(request):
    name = request.POST['name']
    
    u_frontend.add_city(name)
    
    
    return render(request, 'frontend/index.html', {})