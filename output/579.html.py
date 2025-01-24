import requests
                
def get_random_meme():
    api_url = f"https://meme-api.com/gimme"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_meme()

import requests
                
def get_multiple_memes(count):
    api_url = f"https://meme-api.com/gimme/{count}"
    querystring = {'count': count, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_multiple_memes(2)

import requests
                
def get_meme_from_subreddit(subreddit):
    api_url = f"https://meme-api.com/gimme/{subreddit}"
    querystring = {'subreddit': subreddit, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_meme_from_subreddit('wholesomememes')

import requests
                
def get_multiple_memes_from_subreddit(subreddit, count):
    api_url = f"https://meme-api.com/gimme/{subreddit}/{count}"
    querystring = {'subreddit': subreddit, 'count': count, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_multiple_memes_from_subreddit('wholesomememes', 2)

