import requests
                
def get_list_of_all_possible_values_for_the_specified_field(field):
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/list-of/:field"
    querystring = {'field': field, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_all_possible_values_for_the_specified_field('regions')

import requests
                
def fetch_summary():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/summary"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_summary()

import requests
                
def fetch_top_regions():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/top-regions"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_top_regions()

import requests
                
def fetch_no__of_cases_timeline():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/timeline"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_no__of_cases_timeline()

import requests
                
def fetch_raw_data():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/get?page=1&limit=10000"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_raw_data()

import requests
                
def fetch_raw_data_by_month():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/get?month=03"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_raw_data_by_month()

import requests
                
def fetch_raw_data_by_specific_date():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/get?month=03&date=01"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_raw_data_by_specific_date()

import requests
                
def fetch_raw_data_with_filters():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/get?region_res=ncr&age_group=20-24"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_raw_data_with_filters()

import requests
                
def fetch_facilities_summary():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/facilities/summary"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_facilities_summary()

import requests
                
def fetch_list_of_facilities():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/list-of/hospitals?dataset=facilities_information"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_list_of_facilities()

import requests
                
def fetch_raw_facility_hospital_records():
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/facilities"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_raw_facility_hospital_records()

