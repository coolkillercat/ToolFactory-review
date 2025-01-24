import requests
                
def get_all_posts():
    api_url = f"https://jsonplaceholder.typicode.com/posts"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_posts()

import requests
                
def get_post_by_id(id):
    api_url = f"https://jsonplaceholder.typicode.com/posts/1"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_post_by_id(1)

import requests
                
def get_comments_for_post(postId):
    api_url = f"https://jsonplaceholder.typicode.com/posts/1/comments"
    querystring = {'postId': postId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_comments_for_post(1)

import requests
                
def get_comments_by_post_id(postId):
    api_url = f"https://jsonplaceholder.typicode.com/comments?postId=1"
    querystring = {'postId': postId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_comments_by_post_id(1)

import requests
                
def create_a_post(title, body, userId):
    api_url = f"https://jsonplaceholder.typicode.com/posts"
    payload = {'title': title, 'body': body, 'userId': userId, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_a_post('My New Post', 'This is the content of my new post.', 1)

