import requests
                
def get_next_mcu_film():
    api_url = f"https://www.whenisthenextmcufilm.com"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_next_mcu_film()

import requests
                
def get_next_mcu_film__development_():
    api_url = f"https://dev.whenisthenextmcufilm.com"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_next_mcu_film__development_()

