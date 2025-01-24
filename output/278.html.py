import requests
                
def get_all_memes(page):
    api_url = f"http://alpha-meme-maker.herokuapp.com/:page"
    querystring = {'page': 1, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_memes(1)

import requests
                
def add_a_meme(name, tags, image):
    api_url = f"http://alpha-meme-maker.herokuapp.com/add/"
    payload = {'name': name, 'tags': tags, 'image': image, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
add_a_meme('Grumpy Cat', 'funny, cat', 'http://imgflip.com/s/meme/Grumpy-Cat.jpg')

import requests
                
def get_a_meme(id):
    api_url = f"http://alpha-meme-maker.herokuapp.com/memes/:id"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_meme(13)

import requests
                
def get_submissions():
    api_url = f"http://alpha-meme-maker.herokuapp.com/submissions"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_submissions()

import requests
                
def get_submissions_for_a_meme(memeID):
    api_url = f"http://alpha-meme-maker.herokuapp.com/memes/:memeID/submissions"
    querystring = {'memeID': memeID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_submissions_for_a_meme(13)

import requests
                
def add_a_submission(memeID):
    api_url = f"http://alpha-meme-maker.herokuapp.com/submissions"
    payload = {'memeID': memeID, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
add_a_submission(6)

import requests
                
def add_a_submission_for_a_meme(memeID):
    api_url = f"http://alpha-meme-maker.herokuapp.com/memes/:memeID/submissions"
    payload = {'memeID': memeID, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
add_a_submission_for_a_meme(6)

