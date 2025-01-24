import requests
                
def fetch_random_quotes():
    api_url = f"https://zenquotes.io/api/quotes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_random_quotes()

import requests
                
def fetch_quote_of_the_day():
    api_url = f"https://zenquotes.io/api/today"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_quote_of_the_day()

import requests
                
def fetch_random_quote():
    api_url = f"https://zenquotes.io/api/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_random_quote()

import requests
                
def fetch_random_inspirational_image():
    api_url = f"https://zenquotes.io/api/image"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_random_inspirational_image()

import requests
                
def fetch_available_authors(YOUR_KEY):
    api_url = f"https://zenquotes.io/api/authors/[YOUR_KEY]"
    querystring = {'YOUR_KEY': YOUR_KEY, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_available_authors('your_api_key')

import requests
                
def fetch_quotes_by_author(YOUR_KEY):
    api_url = f"https://zenquotes.io/api/quotes/author/sun-tzu/[YOUR_KEY]"
    querystring = {'YOUR_KEY': YOUR_KEY, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_quotes_by_author('your_api_key')

import requests
                
def fetch_quote_image_by_author(YOUR_KEY):
    api_url = f"https://zenquotes.io/api/image/author/sun-tzu/[YOUR_KEY]"
    querystring = {'YOUR_KEY': YOUR_KEY, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_quote_image_by_author('your_api_key')

import requests
                
def fetch_custom_quotes(YOUR_KEY):
    api_url = f"https://zenquotes.io/api/quotes/[YOUR_KEY]&custom=true"
    querystring = {'YOUR_KEY': YOUR_KEY, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_custom_quotes('your_api_key')

import requests
                
def filter_quotes_by_keyword(YOUR_KEY):
    api_url = f"https://zenquotes.io/api/quotes/[YOUR_KEY]&keyword=[keyword]"
    querystring = {'YOUR_KEY': YOUR_KEY, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
filter_quotes_by_keyword('your_api_key')

import requests
                
def generate_quote_image_by_keyword(YOUR_KEY):
    api_url = f"https://zenquotes.io/api/image/[YOUR_KEY]&keyword=[keyword]"
    querystring = {'YOUR_KEY': YOUR_KEY, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_quote_image_by_keyword('your_api_key')

