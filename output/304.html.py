import requests
                
def get_all_books():
    api_url = f"https://wolnelektury.pl/api/books/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_books()

import requests
                
def get_all_audiobooks():
    api_url = f"https://wolnelektury.pl/api/audiobooks/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_audiobooks()

import requests
                
def get_all_daisy_books():
    api_url = f"https://wolnelektury.pl/api/daisy/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_daisy_books()

import requests
                
def get_all_authors():
    api_url = f"https://wolnelektury.pl/api/authors/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_authors()

import requests
                
def get_all_epochs():
    api_url = f"https://wolnelektury.pl/api/epochs/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_epochs()

import requests
                
def get_all_genres():
    api_url = f"https://wolnelektury.pl/api/genres/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_genres()

import requests
                
def get_all_kinds():
    api_url = f"https://wolnelektury.pl/api/kinds/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_kinds()

import requests
                
def get_all_themes():
    api_url = f"https://wolnelektury.pl/api/themes/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_themes()

import requests
                
def get_all_collections():
    api_url = f"https://wolnelektury.pl/api/collections/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_collections()

import requests
                
def get_book_details(book_id):
    api_url = f"missing"
    querystring = {'book_id': book_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_book_details('studnia-i-wahadlo')

import requests
                
def get_author_details(author_id):
    api_url = f"missing"
    querystring = {'author_id': author_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_author_details('edgar-allan-poe')

import requests
                
def get_books_by_author_and_kind(author_id, kind_id):
    api_url = f"missing"
    querystring = {'author_id': author_id, 'kind_id': kind_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_books_by_author_and_kind('adam-mickiewicz', 'liryka')

import requests
                
def get_parent_books_by_author_and_kind(author_id, kind_id):
    api_url = f"missing"
    querystring = {'author_id': author_id, 'kind_id': kind_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_parent_books_by_author_and_kind('adam-mickiewicz', 'liryka')

import requests
                
def get_fragments_by_author_and_theme(author_id, theme_id):
    api_url = f"missing"
    querystring = {'author_id': author_id, 'theme_id': theme_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_fragments_by_author_and_theme('william-shakespeare', 'zabawa')

