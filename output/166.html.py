import requests
                
def get_textual_data(urn):
    api_url = f"https://api.ctext.org/gettext"
    querystring = {'urn': urn, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_textual_data('ctp:analects/xue-er')

import requests
                
def get_status():
    api_url = f"https://api.ctext.org/getstatus"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_status()

import requests
                
def read_link(url):
    api_url = f"https://api.ctext.org/readlink"
    querystring = {'url': url, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
read_link('https://ctext.org/analects/xue-er')

import requests
                
def get_link(urn):
    api_url = f"https://api.ctext.org/getlink"
    querystring = {'urn': urn, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_link('ctp:analects/xue-er')

