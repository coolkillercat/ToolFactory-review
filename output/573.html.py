import requests
                
def list_brands():
    api_url = f"https://api-mobilespecs.azharimm.dev/brands"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_brands()

import requests
                
def list_phones(brand_slug):
    api_url = f"https://api-mobilespecs.azharimm.dev/brands/{brand_slug}"
    querystring = {'brand_slug': brand_slug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_phones('apple-phones-48')

import requests
                
def phone_specifications(brand_slug, phone_slug):
    api_url = f"https://api-mobilespecs.azharimm.dev/brands/{brand_slug}/{phone_slug}"
    querystring = {'brand_slug': brand_slug, 'phone_slug': phone_slug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
phone_specifications('apple', 'apple_iphone_12_pro_max-10237')

import requests
                
def search(query):
    api_url = f"http://api-mobilespecs.azharimm.dev/search"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search('iPhone 12 pro max')

import requests
                
def latest():
    api_url = f"https://api-mobilespecs.azharimm.dev/latest"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
latest()

import requests
                
def top_by_interest():
    api_url = f"https://api-mobilespecs.azharimm.dev/top-by-interest"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
top_by_interest()

import requests
                
def top_by_fans():
    api_url = f"https://api-mobilespecs.azharimm.dev/top-by-fans"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
top_by_fans()

