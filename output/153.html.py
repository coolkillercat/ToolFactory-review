import requests
                
def ip_geolocation_lookup(ip):
    api_url = f"missing"
    querystring = {'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
ip_geolocation_lookup('8.8.4.4')

import requests
                
def asn_information(ip):
    api_url = f"missing"
    querystring = {'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
asn_information('8.8.4.4')

import requests
                
def hosted_domains(ip):
    api_url = f"missing"
    querystring = {'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
hosted_domains('8.8.4.4')

