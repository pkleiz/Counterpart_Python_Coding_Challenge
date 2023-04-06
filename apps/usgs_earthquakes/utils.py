import requests
from apps.logs import utils  as u_logs
from apps.usgs_earthquakes import models as m_usgs_earthquakes
from datetime import datetime

def get_earthquakes(start_date, end_date, minmagnitude):
    
    try:
        basepoint = 'https://earthquake.usgs.gov/fdsnws/event/1/query.geojson'
        
        params = {
            'starttime':start_date,
            'endtime':end_date,
            'minmagnitude':minmagnitude,
            'orderby':'magnitude'
        }
        
        response = requests.get(basepoint, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            u_logs.create_log(response.status_code)
    
    except Exception as e:
        u_logs.create_log(e)
        
def save_earthquakes(response):
    try:
        for feature in response['features']:
            properties = feature['properties']
            geometry = feature['geometry']
            
            earthquake, created = m_usgs_earthquakes.Earthquake.objects.get_or_create(
                magnitude =properties['mag'],
                location = properties['place'],
                title = properties['title'],
                latitude = geometry['coordinates'][1],
                longitude = geometry['coordinates'][0],
                date = datetime.fromtimestamp(properties['time'] / 1000)
            )
            
            if created:
                earthquake.save()
                
    except Exception as e:
        u_logs.create_log(e)