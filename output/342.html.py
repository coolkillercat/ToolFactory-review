import requests
                
def reverse_geocoding(latitude_longitude):
    api_url = f"https://geocode.xyz/latitude,longitude?geoit=outputformat&auth=your_api_key"
    querystring = {'latitude_longitude': latitude_longitude, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
reverse_geocoding('51.50354,-0.12768')

import requests
                
def forward_geocoding(location):
    api_url = f"https://geocode.xyz/location?geoit=outputformat&auth=your_api_key"
    querystring = {'location': location, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
forward_geocoding('Hauptstr., 57632 Berzhausen')

import requests
                
def geoparsing(scantext):
    api_url = f"https://geocode.xyz"
    payload = {'scantext': scantext, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
geoparsing('The most important museums of Amsterdam are located on the Museumplein, located at the southwestern side of the Rijksmuseum.')

import requests
                
def geolocate_ip_address(locate):
    api_url = f"https://geocode.xyz"
    payload = {'locate': locate, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
geolocate_ip_address('203.91.85.36')

import requests
                
def batch_geocoding(locate):
    api_url = f"https://geocode.xyz"
    payload = {'locate': locate, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
batch_geocoding('input.csv')

