import requests
                
def get_list_of_available_servers():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_available_servers()

import requests
                
def get_server_names_via_dns_srv_record():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_server_names_via_dns_srv_record()

import requests
                
def mark_station_as_popular(stationuuid):
    api_url = f"missing"
    querystring = {'stationuuid': stationuuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
mark_station_as_popular('123e4567-e89b-12d3-a456-426614174000')

