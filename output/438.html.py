import requests
                
def get_joke(Category__ies):
    api_url = f"https://v2.jokeapi.dev/joke/[Category/-ies]"
    querystring = {'Category__ies': Category__ies, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_joke('Programming,Misc')

import requests
                
def info():
    api_url = f"https://v2.jokeapi.dev/info"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
info()

import requests
                
def categories():
    api_url = f"https://v2.jokeapi.dev/categories"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
categories()

import requests
                
def language_code(Language):
    api_url = f"https://v2.jokeapi.dev/langcode/[Language]"
    querystring = {'Language': Language, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
language_code('german')

import requests
                
def supported_languages():
    api_url = f"https://v2.jokeapi.dev/languages"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
supported_languages()

import requests
                
def flags():
    api_url = f"https://v2.jokeapi.dev/flags"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
flags()

import requests
                
def formats():
    api_url = f"https://v2.jokeapi.dev/formats"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
formats()

import requests
                
def ping():
    api_url = f"https://v2.jokeapi.dev/ping"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
ping()

import requests
                
def endpoints():
    api_url = f"https://v2.jokeapi.dev/endpoints"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
endpoints()

import requests
                
def submit_joke(formatVersion, category, type, joke, setup, delivery, flags, lang):
    api_url = f"https://v2.jokeapi.dev/submit"
    payload = {'formatVersion': formatVersion, 'category': category, 'type': type, 'joke': joke, 'setup': setup, 'delivery': delivery, 'flags': flags, 'lang': 'en', }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
submit_joke(3, 'Misc', 'single', 'A horse walks into a bar...', 'Why do programmers wear glasses?', 'Because they need to C#', {'nsfw': True, 'religious': False, 'political': True, 'racist': False, 'sexist': False, 'explicit': False}, 'en')

