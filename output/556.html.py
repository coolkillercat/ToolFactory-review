import requests
                
def get_random_cat():
    api_url = f"/cat"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat()

import requests
                
def get_random_cat_by_tag(tag):
    api_url = f"/cat/:tag"
    querystring = {'tag': tag, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_by_tag('cute')

import requests
                
def get_random_cat_gif():
    api_url = f"/cat/gif"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_gif()

import requests
                
def get_random_cat_saying_text(text):
    api_url = f"/cat/says/:text"
    querystring = {'text': text, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_saying_text('hello')

import requests
                
def get_random_cat_by_tag_saying_text(tag, text):
    api_url = f"/cat/:tag/says/:text"
    querystring = {'tag': tag, 'text': text, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_by_tag_saying_text('cute', 'hello')

import requests
                
def get_custom_random_cat_saying_text(text):
    api_url = f"/cat/says/:text?fontSize=:size&fontColor=:color"
    querystring = {'text': text, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_custom_random_cat_saying_text('hello')

import requests
                
def get_random_cat_by_type():
    api_url = f"/cat?type=:type"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_by_type()

import requests
                
def get_random_cat_with_filter():
    api_url = f"/cat?filter=:filter"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_with_filter()

import requests
                
def get_custom_filtered_random_cat():
    api_url = f"/cat?filter=custom&brightness=:brightness&lightness=:lightness&saturation=:saturation&hue=:hue"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_custom_filtered_random_cat()

import requests
                
def get_custom_rgb_filtered_random_cat():
    api_url = f"/cat?filter=custom&r=:red&g=:green&b=:blue"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_custom_rgb_filtered_random_cat()

import requests
                
def get_random_cat_with_custom_size():
    api_url = f"/cat?width=:width or /cat?height=:height"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_with_custom_size()

import requests
                
def get_random_cat_in_html():
    api_url = f"/cat?html=true"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_in_html()

import requests
                
def get_random_cat_in_json():
    api_url = f"/cat?json=true"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_cat_in_json()

import requests
                
def get_all_cats():
    api_url = f"/api/cats?tags=tag1,tag2&skip=0&limit=10"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_cats()

import requests
                
def get_all_tags():
    api_url = f"/api/tags"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_tags()

