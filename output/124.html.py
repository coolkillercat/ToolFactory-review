import requests
                
def get_item(id):
    api_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_item(8863)

import requests
                
def get_user(id):
    api_url = f"https://hacker-news.firebaseio.com/v0/user/{id}.json"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_user('jl')

import requests
                
def get_max_item_id():
    api_url = f"https://hacker-news.firebaseio.com/v0/maxitem.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_max_item_id()

import requests
                
def get_top_stories():
    api_url = f"https://hacker-news.firebaseio.com/v0/topstories.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_top_stories()

import requests
                
def get_new_stories():
    api_url = f"https://hacker-news.firebaseio.com/v0/newstories.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_new_stories()

import requests
                
def get_best_stories():
    api_url = f"https://hacker-news.firebaseio.com/v0/beststories.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_best_stories()

import requests
                
def get_ask_hn_stories():
    api_url = f"https://hacker-news.firebaseio.com/v0/askstories.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_ask_hn_stories()

import requests
                
def get_show_hn_stories():
    api_url = f"https://hacker-news.firebaseio.com/v0/showstories.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_show_hn_stories()

import requests
                
def get_job_stories():
    api_url = f"https://hacker-news.firebaseio.com/v0/jobstories.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_job_stories()

import requests
                
def get_changed_items_and_profiles():
    api_url = f"https://hacker-news.firebaseio.com/v0/updates.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_changed_items_and_profiles()

