import requests
                
def season_list():
    api_url = f"http://ergast.com/api/f1/seasons"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
season_list()

import requests
                
def race_schedule(season):
    api_url = f"http://ergast.com/api/f1/{season}"
    querystring = {'season': season, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
race_schedule(2023)

import requests
                
def race_results(season, round):
    api_url = f"http://ergast.com/api/f1/{season}/{round}/results"
    querystring = {'season': season, 'round': round, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
race_results(2023, 5)

import requests
                
def qualifying_results(season, round):
    api_url = f"http://ergast.com/api/f1/{season}/{round}/qualifying"
    querystring = {'season': season, 'round': round, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
qualifying_results(2023, 5)

import requests
                
def standings(season):
    api_url = f"http://ergast.com/api/f1/{season}/standings"
    querystring = {'season': season, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
standings(2023)

import requests
                
def driver_information():
    api_url = f"http://ergast.com/api/f1/drivers"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
driver_information()

import requests
                
def constructor_information():
    api_url = f"http://ergast.com/api/f1/constructors"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
constructor_information()

import requests
                
def circuit_information():
    api_url = f"http://ergast.com/api/f1/circuits"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
circuit_information()

import requests
                
def finishing_status(season, round):
    api_url = f"http://ergast.com/api/f1/{season}/{round}/status"
    querystring = {'season': season, 'round': round, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
finishing_status(2023, 5)

import requests
                
def lap_times(season, round, driverId):
    api_url = f"http://ergast.com/api/f1/{season}/{round}/drivers/{driverId}/laps"
    querystring = {'season': season, 'round': round, 'driverId': driverId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lap_times(2023, 5, 'hamilton')

import requests
                
def pit_stops(season, round, driverId):
    api_url = f"http://ergast.com/api/f1/{season}/{round}/drivers/{driverId}/pitstops"
    querystring = {'season': season, 'round': round, 'driverId': driverId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
pit_stops(2023, 5, 'hamilton')

