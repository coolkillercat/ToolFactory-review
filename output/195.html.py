import requests
                
def get_all_events_for_a_region(region):
    api_url = f"/api/v1/region/:region/events.json"
    querystring = {'region': region, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_events_for_a_region('Portland')

import requests
                
def get_all_machines_at_locations_in_a_region(region):
    api_url = f"/api/v1/region/:region/location_machine_xrefs.json"
    querystring = {'region': region, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_machines_at_locations_in_a_region('Portland')

import requests
                
def get_info_about_a_single_lmx(id):
    api_url = f"/api/v1/location_machine_xrefs/:id.json"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_info_about_a_single_lmx(123)

import requests
                
def find_or_create_a_machine_at_a_location(location_id, machine_id):
    api_url = f"/api/v1/location_machine_xrefs.json"
    payload = {'location_id': location_id, 'machine_id': machine_id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
find_or_create_a_machine_at_a_location(456, 789)

import requests
                
def show_the_top_n_machines_on_location():
    api_url = f"/api/v1/location_machine_xrefs/top_n_machines.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
show_the_top_n_machines_on_location()

import requests
                
def returns_the_most_recently_added_machines_near_transmitted_lat_lon(lat, lon):
    api_url = f"/api/v1/location_machine_xrefs/most_recent_by_lat_lon.json"
    querystring = {'lat': lat, 'lon': lon, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
returns_the_most_recently_added_machines_near_transmitted_lat_lon('45.523064', '-122.676483')

import requests
                
def get_info_about_a_single_lpx(id):
    api_url = f"/api/v1/location_picture_xrefs/:id.json"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_info_about_a_single_lpx(123)

import requests
                
def add_a_picture_for_a_location(location_id, photo):
    api_url = f"/api/v1/location_picture_xrefs.json"
    payload = {'location_id': location_id, 'photo': photo, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
add_a_picture_for_a_location(456, image.jpg)

import requests
                
def fetch_all_location_types():
    api_url = f"/api/v1/location_types.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_all_location_types()

import requests
                
def suggest_a_new_location_to_add_to_the_map(location_name):
    api_url = f"/api/v1/locations/suggest.json"
    payload = {'location_name': location_name, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
suggest_a_new_location_to_add_to_the_map('Pinball Palace')

import requests
                
def fetch_locations_for_all_regions():
    api_url = f"/api/v1/locations.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_locations_for_all_regions()

import requests
                
def returns_the_closest_location_to_transmitted_lat_lon(lat, lon):
    api_url = f"/api/v1/locations/closest_by_lat_lon.json"
    querystring = {'lat': lat, 'lon': lon, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
returns_the_closest_location_to_transmitted_lat_lon('45.523064', '-')

