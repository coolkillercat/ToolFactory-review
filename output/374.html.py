import requests
                
def lookup_a_postcode(postcode):
    api_url = f"https://api.postcodes.io/postcodes/{postcode}"
    querystring = {'postcode': postcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lookup_a_postcode('OX49 5NU')

import requests
                
def bulk_lookup_postcodes(postcodes):
    api_url = f"https://api.postcodes.io/postcodes"
    payload = {'postcodes': postcodes, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
bulk_lookup_postcodes(['OX49 5NU', 'M32 0JG', 'NE30 1DP'])

import requests
                
def get_nearest_postcodes_for_a_given_longitude___latitude(longitude, latitude):
    api_url = f"https://api.postcodes.io/postcodes?lon={longitude}&lat={latitude}"
    querystring = {'longitude': longitude, 'latitude': latitude, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_nearest_postcodes_for_a_given_longitude___latitude(0.629834723775309, 51.7923246977375)

import requests
                
def bulk_reverse_geocoding(geolocations):
    api_url = f"https://api.postcodes.io/postcodes"
    payload = {'geolocations': geolocations, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
bulk_reverse_geocoding([{'longitude': 0.629834723775309, 'latitude': 51.7923246977375}, {'longitude': -2.49690382054704, 'latitude': 53.5351312861402, 'radius': 1000, 'limit': 5}])

import requests
                
def get_a_random_postcode():
    api_url = f"https://api.postcodes.io/random/postcodes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_random_postcode()

import requests
                
def validate_a_postcode(postcode):
    api_url = f"https://api.postcodes.io/postcodes/{postcode}/validate"
    querystring = {'postcode': postcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
validate_a_postcode('OX49 5NU')

import requests
                
def nearest_postcodes_for_postcode(postcode):
    api_url = f"https://api.postcodes.io/postcodes/{postcode}/nearest"
    querystring = {'postcode': postcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
nearest_postcodes_for_postcode('OX49 5NU')

import requests
                
def autocomplete_a_postcode_partial(partial):
    api_url = f"https://api.postcodes.io/postcodes/{partial}/autocomplete"
    querystring = {'partial': partial, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
autocomplete_a_postcode_partial('OX49')

import requests
                
def query_for_postcode(query):
    api_url = f"https://api.postcodes.io/postcodes?q={query}"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_for_postcode('OX49 5NU')

import requests
                
def lookup_terminated_postcode(postcode):
    api_url = f"https://api.postcodes.io/terminated_postcodes/{postcode}"
    querystring = {'postcode': postcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lookup_terminated_postcode('OX49 5NU')

import requests
                
def lookup_outward_code(outcode):
    api_url = f"https://api.postcodes.io/outcodes/{outcode}"
    querystring = {'outcode': outcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lookup_outward_code('OX49')

import requests
                
def nearest_outward_code_for_outward_code(outcode):
    api_url = f"https://api.postcodes.io/outcodes/{outcode}/nearest"
    querystring = {'outcode': outcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
nearest_outward_code_for_outward_code('OX49')

import requests
                
def get_nearest_outward_codes_for_a_given_longitude___latitude(longitude, latitude):
    api_url = f"https://api.postcodes.io/outcodes?lon={longitude}&lat={latitude}"
    querystring = {'longitude': longitude, 'latitude': latitude, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_nearest_outward_codes_for_a_given_longitude___latitude(0.629834723775309, 51.7923246977375)

