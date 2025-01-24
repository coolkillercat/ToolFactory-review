import requests
                
def get_current_stable_version():
    api_url = f"https://namo-memes.herokuapp.com/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_current_stable_version()

import requests
                
def get_random_memes(n):
    api_url = f"https://namo-memes.herokuapp.com/memes/:n"
    querystring = {'n': n, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_memes(5)

import requests
                
def get_memes_with_pagination(page, n):
    api_url = f"https://namo-memes.herokuapp.com/memes/page/:page/:n"
    querystring = {'page': page, 'n': n, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_memes_with_pagination(1, 10)

import requests
                
def get_latest_memes(n):
    api_url = f"https://namo-memes.herokuapp.com/memes/latest/:n"
    querystring = {'n': n, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_latest_memes(5)

