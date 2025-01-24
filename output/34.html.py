import requests
                
def get_election_data():
    api_url = f"https://uselection.togatech.org/api/data"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_election_data()

import requests
                
def get_metadata():
    api_url = f"https://uselection.togatech.org/api/metadata"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_metadata()

import requests
                
def get_parties():
    api_url = f"https://uselection.togatech.org/api/parties"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_parties()

import requests
                
def get_votes():
    api_url = f"https://uselection.togatech.org/api/votes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_votes()

