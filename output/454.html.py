import requests
                
def universal_endpoint(query):
    api_url = f"http://127.0.0.1:5000/result/"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
universal_endpoint('alone')

import requests
                
def song_url_endpoint(query):
    api_url = f"http://127.0.0.1:5000/song/"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
song_url_endpoint('https://www.jiosaavn.com/song/khairiyat/PwAFSRNpAWw')

import requests
                
def playlist_url_endpoint(query):
    api_url = f"http://127.0.0.1:5000/playlist/"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
playlist_url_endpoint('https://www.jiosaavn.com/featured/romantic-hits-2020---hindi/ABiMGqjovSFuOxiEGmm6lQ')

import requests
                
def album_url_endpoint(query):
    api_url = f"http://127.0.0.1:5000/album/"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
album_url_endpoint('https://www.jiosaavn.com/album/chhichhore/V4F3M5,cNb4')

import requests
                
def lyrics_endpoint(query):
    api_url = f"http://127.0.0.1:5000/lyrics/"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lyrics_endpoint('https://www.jiosaavn.com/song/khairiyat/PwAFSRNpAWw')

