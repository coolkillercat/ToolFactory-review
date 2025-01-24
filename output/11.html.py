import requests
                
def list_all_covid_19_cases_per_country():
    api_url = f"https://covid-19.dataflowkit.com/v1"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_all_covid_19_cases_per_country()

import requests
                
def get_covid_19_cases_for_a_specific_country(country):
    api_url = f"https://covid-19.dataflowkit.com/v1/{country}"
    querystring = {'country': country, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_covid_19_cases_for_a_specific_country('USA')

