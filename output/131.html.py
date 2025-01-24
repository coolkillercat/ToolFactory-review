import requests
                
def manual_mode(lang, ip):
    api_url = f"https://hellosalut.stefanbohacek.dev/"
    querystring = {'lang': lang, 'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
manual_mode('en', '89.120.120.120')

import requests
                
def automatic_mode():
    api_url = f"https://hellosalut.stefanbohacek.dev/?mode=auto"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
automatic_mode()

