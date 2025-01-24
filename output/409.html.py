import requests
                
def search(q):
    api_url = f"https://nominatim.openstreetmap.org/search"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search('Berlin')

import requests
                
def reverse(lat, lon):
    api_url = f"https://nominatim.openstreetmap.org/reverse"
    querystring = {'lat': lat, 'lon': lon, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
reverse(52.52, 13.405)

import requests
                
def lookup(osm_ids):
    api_url = f"https://nominatim.openstreetmap.org/lookup"
    querystring = {'osm_ids': osm_ids, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lookup('R146656,W104393803,N240109189')

import requests
                
def status():
    api_url = f"https://nominatim.openstreetmap.org/status"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
status()

import requests
                
def deletable():
    api_url = f"https://nominatim.openstreetmap.org/deletable"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
deletable()

import requests
                
def polygons():
    api_url = f"https://nominatim.openstreetmap.org/polygons"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
polygons()

import requests
                
def details(osm_id):
    api_url = f"https://nominatim.openstreetmap.org/details"
    querystring = {'osm_id': osm_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
details('R146656')

