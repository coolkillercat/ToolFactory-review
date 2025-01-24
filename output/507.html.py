import requests
                
def get_bank_name_by_routing_number(routingNumber):
    api_url = f"missing"
    querystring = {'routingNumber': routingNumber, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_bank_name_by_routing_number('123456789')

import requests
                
def get_all_information_by_routing_number(routingNumber):
    api_url = f"missing"
    querystring = {'routingNumber': routingNumber, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_information_by_routing_number('123456789')

import requests
                
def lookup_routing_numbers():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lookup_routing_numbers()

