import requests
                
def serve_file_from_github(user, repo, tag, file):
    api_url = f"https://cdn.statically.io/gh/:user/:repo/:tag/:file"
    querystring = {'user': user, 'repo': repo, 'tag': tag, 'file': file, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
serve_file_from_github('octocat', 'Hello-World', 'main', 'index.html')

import requests
                
def serve_file_from_gitlab(user, repo, tag, file):
    api_url = f"https://cdn.statically.io/gl/:user/:repo/:tag/:file"
    querystring = {'user': user, 'repo': repo, 'tag': tag, 'file': file, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
serve_file_from_gitlab('john_doe', 'project-repo', 'main', 'style.css')

import requests
                
def serve_file_from_bitbucket(user, repo, tag, file):
    api_url = f"https://cdn.statically.io/bb/:user/:repo/:tag/:file"
    querystring = {'user': user, 'repo': repo, 'tag': tag, 'file': file, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
serve_file_from_bitbucket('jane_doe', 'my-repo', 'main', 'script.js')

import requests
                
def live_demo():
    api_url = f"https://cdn.statically.io/gh/mrdoob/three.js/dev/build/three.min.js"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
live_demo()

