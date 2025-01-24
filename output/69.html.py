import requests
                
def find_elected_officials_by_postal_code(postal_code):
    api_url = f"missing"
    querystring = {'postal_code': postal_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
find_elected_officials_by_postal_code('K1A0B1')

import requests
                
def find_elected_officials_by_geocoded_address(latitude, longitude):
    api_url = f"missing"
    querystring = {'latitude': latitude, 'longitude': longitude, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
find_elected_officials_by_geocoded_address(45.4215, -75.6972)

import requests
                
def find_electoral_district_by_postal_code(postal_code):
    api_url = f"missing"
    querystring = {'postal_code': postal_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
find_electoral_district_by_postal_code('K1A0B1')

import requests
                
def find_electoral_district_by_geocoded_address(latitude, longitude):
    api_url = f"missing"
    querystring = {'latitude': latitude, 'longitude': longitude, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
find_electoral_district_by_geocoded_address(45.4215, -75.6972)

