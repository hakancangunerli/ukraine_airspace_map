import requests
import json
def api_call(lat_min, lon_min, lat_max, lon_max):
    #REST API QUERY
    url_data = 'https://'+''+''+'opensky-network.org/api/states/all?' + \
    'lamin='+str(lat_min)+'&lomin='+str(lon_min)+'&lamax=' + \
    str(lat_max)+'&lomax='+str(lon_max)
    response = requests.get(url_data).json()
    return response 
