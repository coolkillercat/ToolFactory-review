import requests
                
def search(term):
    api_url = f"https://unofficialurbandictionaryapi.com/api/search"
    querystring = {'term': term, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search('yeet')

import requests
                
def random():
    api_url = f"https://unofficialurbandictionaryapi.com/api/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
random()

import requests
                
def browse():
    api_url = f"https://unofficialurbandictionaryapi.com/api/browse"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
browse()

import requests
                
def author(author):
    api_url = f"https://unofficialurbandictionaryapi.com/api/author"
    querystring = {'author': author, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
author('Aaron Peckham')

import requests
                
def date(date):
    api_url = f"https://unofficialurbandictionaryapi.com/api/date"
    querystring = {'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
date('2023-01-01')

