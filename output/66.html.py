import requests
                
def station_stop_api(station_or_stop):
    api_url = f"missing"
    querystring = {'station_or_stop': station_or_stop, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
station_stop_api('finch_station')

import requests
                
def undocumented_api___near_location(latitude, longitude):
    api_url = f"missing"
    querystring = {'latitude': latitude, 'longitude': longitude, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
undocumented_api___near_location(43.6557074, -79.3850234)

import requests
                
def undocumented_api___near_intersection(intersection):
    api_url = f"missing"
    querystring = {'intersection': intersection, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
undocumented_api___near_intersection('steeles_and_bathurst')

import requests
                
def undocumented_api___vehicles_near_intersection(intersection):
    api_url = f"missing"
    querystring = {'intersection': intersection, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
undocumented_api___vehicles_near_intersection('bay_and_dundas')

