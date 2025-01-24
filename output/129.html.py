import requests
                
def get_work_metadata(doi):
    api_url = f"https://api.crossref.org/works/{doi}"
    querystring = {'doi': doi, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_work_metadata('10.1037/0003-066X.59.1.29')

import requests
                
def get_funder_metadata(funder_id):
    api_url = f"https://api.crossref.org/funders/{funder_id}"
    querystring = {'funder_id': funder_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_funder_metadata('100000015')

import requests
                
def get_member_metadata(member_id):
    api_url = f"https://api.crossref.org/members/{member_id}"
    querystring = {'member_id': member_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_member_metadata('98')

import requests
                
def get_journal_metadata(issn):
    api_url = f"https://api.crossref.org/journals/{issn}"
    querystring = {'issn': issn, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_journal_metadata('1549-7712')

import requests
                
def search_works():
    api_url = f"https://api.crossref.org/works"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_works()

import requests
                
def get_work_agency(doi):
    api_url = f"https://api.crossref.org/works/{doi}/agency"
    querystring = {'doi': doi, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_work_agency('10.1037/0003-066X.59.1.29')

