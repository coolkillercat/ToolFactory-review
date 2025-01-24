import requests
                
def get_memes():
    api_url = f"https://api.imgflip.com/get_memes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_memes()

import requests
                
def caption_image(template_id, username, password):
    api_url = f"https://api.imgflip.com/caption_image"
    payload = {'template_id': template_id, 'username': username, 'password': password, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
caption_image('61579', 'user123', 'password123')

import requests
                
def search_memes(username, password, query):
    api_url = f"https://api.imgflip.com/search_memes"
    payload = {'username': username, 'password': password, 'query': query, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_memes('user123', 'password123', 'funny')

import requests
                
def automeme(username, password, text):
    api_url = f"https://api.imgflip.com/automeme"
    payload = {'username': username, 'password': password, 'text': text, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
automeme('user123', 'password123', 'This is a meme')

import requests
                
def ai_meme(username, password):
    api_url = f"https://api.imgflip.com/ai_meme"
    payload = {'username': username, 'password': password, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
ai_meme('user123', 'password123')

