import requests
                
def get_authors():
    api_url = f"https://poetrydb.org/author"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_authors()

import requests
                
def get_author_details(author):
    api_url = f"https://poetrydb.org/author/{author}"
    querystring = {'author': author, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_author_details('William Shakespeare')

import requests
                
def get_titles():
    api_url = f"https://poetrydb.org/title"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_titles()

import requests
                
def get_title_details(title):
    api_url = f"https://poetrydb.org/title/{title}"
    querystring = {'title': title, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_title_details('Ozymandias')

import requests
                
def get_lines(lines):
    api_url = f"https://poetrydb.org/lines/{lines}"
    querystring = {'lines': lines, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_lines('Latitudeless Place')

import requests
                
def get_poems_by_line_count(linecount):
    api_url = f"https://poetrydb.org/linecount/{linecount}"
    querystring = {'linecount': linecount, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_poems_by_line_count(14)

import requests
                
def get_random_poems(random_count):
    api_url = f"https://poetrydb.org/random/{random_count}"
    querystring = {'random_count': random_count, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_poems(3)

import requests
                
def get_poems_by_combination(input_field1, input_field2, search_term1, search_term2):
    api_url = f"https://poetrydb.org/{input_field1},{input_field2}/{search_term1};{search_term2}"
    querystring = {'input_field1': input_field1, 'input_field2': input_field2, 'search_term1': search_term1, 'search_term2': search_term2, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_poems_by_combination('title', 'author', 'Winter', 'William Shakespeare')

