import requests
                
def get_forecast(office, gridX, gridY):
    api_url = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"
    querystring = {'office': office, 'gridX': gridX, 'gridY': gridY, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_forecast('TOP', 31, 80)

import requests
                
def get_point_forecast(latitude, longitude):
    api_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    querystring = {'latitude': latitude, 'longitude': longitude, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_point_forecast(39.7456, -97.0892)

import requests
                
def get_active_alerts(state):
    api_url = f"https://api.weather.gov/alerts/active?area={state}"
    querystring = {'state': state, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_active_alerts('KS')

