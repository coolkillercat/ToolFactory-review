import requests
                
def get_public_ip__ipv4_():
    api_url = f"https://api.ipify.org"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_public_ip__ipv4_()

import requests
                
def get_public_ip__ipv6_():
    api_url = f"https://api6.ipify.org"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_public_ip__ipv6_()

import requests
                
def get_public_ip__universal__ipv4_ipv6_():
    api_url = f"https://api64.ipify.org"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_public_ip__universal__ipv4_ipv6_()

