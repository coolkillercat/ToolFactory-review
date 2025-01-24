import requests
                
def get_summary():
    api_url = f"https://status.digitalocean.com/api/v2/summary.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_summary()

import requests
                
def get_status():
    api_url = f"https://status.digitalocean.com/api/v2/status.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_status()

import requests
                
def get_components():
    api_url = f"https://status.digitalocean.com/api/v2/components.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_components()

import requests
                
def get_unresolved_incidents():
    api_url = f"https://status.digitalocean.com/api/v2/incidents/unresolved.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_unresolved_incidents()

import requests
                
def get_all_incidents():
    api_url = f"https://status.digitalocean.com/api/v2/incidents.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_incidents()

import requests
                
def get_upcoming_scheduled_maintenances():
    api_url = f"https://status.digitalocean.com/api/v2/scheduled-maintenances/upcoming.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_upcoming_scheduled_maintenances()

import requests
                
def get_active_scheduled_maintenances():
    api_url = f"https://status.digitalocean.com/api/v2/scheduled-maintenances/active.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_active_scheduled_maintenances()

import requests
                
def get_all_scheduled_maintenances():
    api_url = f"https://status.digitalocean.com/api/v2/scheduled-maintenances.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_scheduled_maintenances()

