import requests
                
def world_topology_data():
    api_url = f"https://power.lowyinstitute.org/world.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
world_topology_data()

import requests
                
def list_of_all_countries():
    api_url = f"https://power.lowyinstitute.org/countries.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_of_all_countries()

import requests
                
def country_data(country_slug):
    api_url = f"https://power.lowyinstitute.org/{country_slug}.json"
    querystring = {'country_slug': country_slug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
country_data('australia')

import requests
                
def country_data_by_year(Year):
    api_url = f"https://power.lowyinstitute.org/data/{Year}.json"
    querystring = {'Year': Year, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
country_data_by_year(2022)

import requests
                
def network_power_data():
    api_url = f"https://power.lowyinstitute.org/network-power.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
network_power_data()

