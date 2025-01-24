import requests
                
def lookup_single_ip_address_or_asn(q):
    api_url = f"https://api.ipapi.is"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lookup_single_ip_address_or_asn('3.5.140.2')

import requests
                
def bulk_ip_address_lookup(ips):
    api_url = f"https://api.ipapi.is"
    payload = {'ips': ips, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
bulk_ip_address_lookup(['162.158.0.0', '2406:dafe:e0ff:ffff:ffff:ffff:dead:beef', '162.88.0.0', '20.41.193.225'])

