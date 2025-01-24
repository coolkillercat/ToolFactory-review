import requests
                
def get_all_groundhogs():
    api_url = f"https://groundhog-day.com/api/v1/groundhogs"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_groundhogs()

import requests
                
def get_groundhog_by_slug(slug):
    api_url = f"https://groundhog-day.com/api/v1/groundhogs/{slug}"
    querystring = {'slug': slug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_groundhog_by_slug('punxsutawney-phil')

import requests
                
def get_predictions_by_year(year):
    api_url = f"https://groundhog-day.com/api/v1/predictions?year={year}"
    querystring = {'year': year, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_predictions_by_year(2023)

