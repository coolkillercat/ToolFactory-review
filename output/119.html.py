import requests
                
def complete_location_of_specific_ip(ip, format):
    api_url = f"https://ipapi.co/{ip}/{format}/"
    querystring = {'ip': ip, 'format': 'json', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
complete_location_of_specific_ip('8.8.8.8', 'json')

import requests
                
def specific_location_field_of_specific_ip(ip, field):
    api_url = f"https://ipapi.co/{ip}/{field}/"
    querystring = {'ip': ip, 'field': field, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
specific_location_field_of_specific_ip('8.8.8.8', 'country')

import requests
                
def complete_location_of_client_s_ip(format):
    api_url = f"https://ipapi.co/{format}/"
    querystring = {'format': 'json', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
complete_location_of_client_s_ip('json')

import requests
                
def specific_location_field_of_client_s_ip(field):
    api_url = f"https://ipapi.co/{field}/"
    querystring = {'field': field, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
specific_location_field_of_client_s_ip('ip')

