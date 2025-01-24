import requests
                
def get_random_useless_fact():
    api_url = f"/api/v2/facts/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_useless_fact()

import requests
                
def get_today_s_useless_fact():
    api_url = f"/api/v2/facts/today"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_today_s_useless_fact()

