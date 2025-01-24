import requests
                
def get_random_cat_fact():
    api_url = f"https://meowfacts.herokuapp.com/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_fact()

import requests
                
def get_multiple_cat_facts():
    api_url = f"https://meowfacts.herokuapp.com/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_multiple_cat_facts()

import requests
                
def get_specific_cat_fact():
    api_url = f"https://meowfacts.herokuapp.com/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_specific_cat_fact()

import requests
                
def get_cat_facts_in_different_language():
    api_url = f"https://meowfacts.herokuapp.com/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_cat_facts_in_different_language()

