from requests.auth import HTTPBasicAuth
from django.conf import settings
import requests


def add_city(city):
    url = settings.BASE_POINT+'cities/'
    data = {'name': city}

    response = requests.post(url, params=data, auth=HTTPBasicAuth(settings.USER, settings.PASS))

    if response.status_code == 200:
        return "Ok"
    else:
        return "fail"
