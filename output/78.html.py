import requests
                
def get_capacity_data():
    api_url = f"https://bcferriesapi.ca/v2/capacity"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_capacity_data()

import requests
                
def get_non_capacity_data():
    api_url = f"https://bcferriesapi.ca/v2/noncapacity/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_non_capacity_data()

