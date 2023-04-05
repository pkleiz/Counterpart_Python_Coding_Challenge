import requests
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse


def custom_post_view(request):
    url = 'http://127.0.0.1:2020/earthquakes/'
    data = {'start_date': '2021-02-01', 'end_date': '2021-02-12'}
    response = requests.get(url, data=data, auth=HTTPBasicAuth('pkleiz', '123'))
    return HttpResponse(response)
