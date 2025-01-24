import requests
                
def get_national_population_data():
    api_url = f"https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_national_population_data()

import requests
                
def get_state_population_data():
    api_url = f"https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_state_population_data()

