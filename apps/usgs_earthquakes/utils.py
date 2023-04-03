import requests
from apps.logs import utils  as u_logs

def get_earthquakes(starttime, endtime, minmagnitude=5.1):
    
    try:
        basepoint = 'https://earthquake.usgs.gov/fdsnws/event/1/query.geojson'
        
        params = {
            'starttime':starttime,
            'endtime':endtime,
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