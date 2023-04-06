from urllib.request import HTTPBasicAuthHandler
from django.conf import settings
import requests


def add_city(city):
    url = settings.BASE_POINT+'cities/'
    data = {'name': city}

    response = requests.post(url, data=data, auth=HTTPBasicAuthHandler('pkleiz', '123'))

    if response.status_code == 200:
        return "Ok"
    else:
        return "fail"
