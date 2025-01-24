import requests
                
def github_stats_card(username):
    api_url = f"https://github-readme-stats.vercel.app/api"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
github_stats_card('anuraghazra')

import requests
                
def top_languages_card(username):
    api_url = f"https://github-readme-stats.vercel.app/api/top-langs"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
top_languages_card('anuraghazra')

import requests
                
def github_gist_pins(id):
    api_url = f"https://github-readme-stats.vercel.app/api/gist"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
github_gist_pins('bbfce31e0217a3689c8d961a356cb10d')

import requests
                
def github_extra_pins(username, repo):
    api_url = f"https://github-readme-stats.vercel.app/api/pin"
    querystring = {'username': username, 'repo': repo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
github_extra_pins('anuraghazra', 'github-readme-stats')

import requests
                
def wakatime_stats_card(username):
    api_url = f"https://github-readme-stats.vercel.app/api/wakatime"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
wakatime_stats_card('ffflabs')

