import requests
                
def daily_numbers():
    api_url = f"https://data.covid19india.org/v4/min/timeseries.min.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
daily_numbers()

import requests
                
def current_day_numbers():
    api_url = f"https://data.covid19india.org/v4/min/data.min.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
current_day_numbers()

