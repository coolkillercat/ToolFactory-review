import requests
                
def random_advice():
    api_url = f"https://api.adviceslip.com/advice"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
random_advice()

import requests
                
def advice_by_id():
    api_url = f"https://api.adviceslip.com/advice/{slip_id}"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
advice_by_id()

import requests
                
def searching_advice():
    api_url = f"https://api.adviceslip.com/advice/search/{query}"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
searching_advice()

import requests
                
def daily_advice_slip_rss_feed():
    api_url = f"https://api.adviceslip.com/daily_adviceslip.rss"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
daily_advice_slip_rss_feed()

