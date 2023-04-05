from geopy.distance import geodesic
import requests
import urllib.parse
from apps.logs import utils as u_logs

def get_distance(lat1, long1, earthquakes):
    try:
        place1 = (lat1, long1)
        nearest_earthquake = "No results found"
        nearest_earthquake_km = 50000
        
        for earthquake in earthquakes:
            place2 = (earthquake.latitude, earthquake.longitude)
            
            if(geodesic(place1, place2).km < nearest_earthquake_km):
                nearest_earthquake_km = geodesic(place1, place2).km
                nearest_earthquake = earthquake
                
        if(nearest_earthquake == 'No results found'):
            nearest_earthquake_km = None
            nearest_earthquake = None
        return [nearest_earthquake, nearest_earthquake_km] 
                
    except Exception as e:
        u_logs.create_log(e)
        
def get_lat_long(address):
    try:
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

        response = requests.get(url).json()
        
        return [response[0]["lat"], response[0]["lon"]]
    
    except Exception as e:
        u_logs.create_log(e)
        return [0, 0, "could not find the location, please try again or insert manually."]
        
        

    