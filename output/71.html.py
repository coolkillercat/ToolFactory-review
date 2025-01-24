import requests
                
def get_ip_details(token):
    api_url = f"https://ipinfo.io/{ip}?token={TOKEN}"
    querystring = {'token': token, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_ip_details('YOUR_API_TOKEN')

import requests
                
def get_ip_details_with_jsonp(token, callback):
    api_url = f"https://ipinfo.io/json?callback={callback}&token={TOKEN}"
    querystring = {'token': token, 'callback': callback, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_ip_details_with_jsonp('YOUR_API_TOKEN', 'recordData')

import requests
                
def filter_ip_details(token, field):
    api_url = f"https://ipinfo.io/{ip}/{field}?token={TOKEN}"
    querystring = {'token': token, 'field': field, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
filter_ip_details('YOUR_API_TOKEN', 'city')

