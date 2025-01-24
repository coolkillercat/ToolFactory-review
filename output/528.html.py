import requests
                
def get_all_dog_facts():
    api_url = f"https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_dog_facts()

import requests
                
def get_specific_number_of_dog_facts(number):
    api_url = f"https://dog-facts-api.herokuapp.com/api/v1/resources/dogs"
    querystring = {'number': number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_specific_number_of_dog_facts(1)

import requests
                
def get_dog_fact_by_index(index):
    api_url = f"https://dog-facts-api.herokuapp.com/api/v1/resources/dogs"
    querystring = {'index': index, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_dog_fact_by_index(0)

