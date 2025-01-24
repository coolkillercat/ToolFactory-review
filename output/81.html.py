import requests
                
def national_data_historic_us_values():
    api_url = f"https://api.covidtracking.com/v2/us/daily.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
national_data_historic_us_values()

import requests
                
def single_day_of_data_for_the_us(date_iso_format):
    api_url = f"https://api.covidtracking.com/v2/us/daily/[date-iso-format].json"
    querystring = {'date_iso_format': date_iso_format, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
single_day_of_data_for_the_us('2021-01-02')

import requests
                
def simplified_single_day_of_data_for_the_us(date_iso_format):
    api_url = f"https://api.covidtracking.com/v2/us/daily/[date-iso-format]/simple.json"
    querystring = {'date_iso_format': date_iso_format, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
simplified_single_day_of_data_for_the_us('2021-01-02')

import requests
                
def all_state_metadata():
    api_url = f"https://api.covidtracking.com/v2/states.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_state_metadata()

import requests
                
def single_state_metadata(state_code):
    api_url = f"https://api.covidtracking.com/v2/states/[state-code].json"
    querystring = {'state_code': state_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
single_state_metadata('mi')

import requests
                
def historic_data_for_a_state_or_territory(state_code):
    api_url = f"https://api.covidtracking.com/v2/states/[state-code]/daily.json"
    querystring = {'state_code': state_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
historic_data_for_a_state_or_territory('ca')

import requests
                
def simplified_historic_data_for_a_state_or_territory(state_code):
    api_url = f"https://api.covidtracking.com/v2/states/[state-code]/daily/simple.json"
    querystring = {'state_code': state_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
simplified_historic_data_for_a_state_or_territory('ca')

import requests
                
def single_day_of_data_for_a_state_or_territory(state_code, date_iso_format):
    api_url = f"https://api.covidtracking.com/v2/states/[state-code]/[date-iso-format].json"
    querystring = {'state_code': state_code, 'date_iso_format': date_iso_format, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
single_day_of_data_for_a_state_or_territory('ca', '2021-01-10')

import requests
                
def simplified_single_day_of_data_for_a_state_or_territory(state_code, date_iso_format):
    api_url = f"https://api.covidtracking.com/v2/states/[state-code]/[date-iso-format]/simple.json"
    querystring = {'state_code': state_code, 'date_iso_format': date_iso_format, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
simplified_single_day_of_data_for_a_state_or_territory('ca', '2021-01-10')

