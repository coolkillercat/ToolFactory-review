import requests
                
def get_subdomains(domain):
    api_url = f"https://sonar.omnisint.io/subdomains/{domain}"
    querystring = {'domain': domain, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_subdomains('example.com')

import requests
                
def get_tlds(domain):
    api_url = f"https://sonar.omnisint.io/tlds/{domain}"
    querystring = {'domain': domain, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_tlds('example.com')

import requests
                
def get_all_results(domain):
    api_url = f"https://sonar.omnisint.io/all/{domain}"
    querystring = {'domain': domain, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_results('example.com')

import requests
                
def reverse_dns_lookup(ip):
    api_url = f"https://sonar.omnisint.io/reverse/{ip}"
    querystring = {'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
reverse_dns_lookup('8.8.8.8')

import requests
                
def reverse_dns_lookup_for_cidr_range(ip, mask):
    api_url = f"https://sonar.omnisint.io/reverse/{ip}/{mask}"
    querystring = {'ip': ip, 'mask': mask, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
reverse_dns_lookup_for_cidr_range('8.8.8.0', '24')

