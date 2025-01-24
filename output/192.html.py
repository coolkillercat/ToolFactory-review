import requests
                
def geolocation_api(ip):
    api_url = f"missing"
    querystring = {'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
geolocation_api('8.8.8.8')

import requests
                
def batch_api(ips):
    api_url = f"missing"
    payload = {'ips': ips, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
batch_api(['8.8.8.8', '8.8.4.4'])

import requests
                
def dns_api(domain):
    api_url = f"missing"
    querystring = {'domain': domain, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
dns_api('example.com')

