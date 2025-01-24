import requests
                
def current_iss_location():
    api_url = f"http://api.open-notify.org/iss-now.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
current_iss_location()

import requests
                
def number_of_people_in_space():
    api_url = f"http://api.open-notify.org/astros.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
number_of_people_in_space()

