import requests
                
def get_random_taco():
    api_url = f"http://taco-randomizer.herokuapp.com/random/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_taco()

import requests
                
def get_contributors_for_recipe(recipe_type, recipe_slug):
    api_url = f"http://taco-randomizer.herokuapp.com/contributors/:recipe_type/:recipe_slug/"
    querystring = {'recipe_type': recipe_type, 'recipe_slug': recipe_slug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_contributors_for_recipe('base_layers', 'delengua_beef_tongue')

import requests
                
def get_recipe_slugs(recipe_type):
    api_url = f"http://taco-randomizer.herokuapp.com/contributors/:recipe_type/"
    querystring = {'recipe_type': recipe_type, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_recipe_slugs('mixins')

import requests
                
def get_contributions_by_user(github_username):
    api_url = f"http://taco-randomizer.herokuapp.com/contributions/:github_username/"
    querystring = {'github_username': github_username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_contributions_by_user('sinker')

import requests
                
def get_all_contributors():
    api_url = f"http://taco-randomizer.herokuapp.com/contributions/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_contributors()

