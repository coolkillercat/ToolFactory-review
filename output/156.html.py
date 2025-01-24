import requests
                
def list_tenders():
    api_url = f"https://tenders.guru/api/es/tenders"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_tenders()

import requests
                
def get_tender_details(tender_id):
    api_url = f"https://tenders.guru/api/es/tenders/{tender_id}"
    querystring = {'tender_id': tender_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_tender_details(123)

import requests
                
def get_tender_source_data(tender_id):
    api_url = f"https://tenders.guru/api/es/tenders/{tender_id}/source_data"
    querystring = {'tender_id': tender_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_tender_source_data(123)

import requests
                
def list_tender_notices(tender_id):
    api_url = f"https://tenders.guru/api/es/tenders/{tender_id}/notices"
    querystring = {'tender_id': tender_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_tender_notices(123)

import requests
                
def list_tender_documents(tender_id):
    api_url = f"https://tenders.guru/api/es/tenders/{tender_id}/docs"
    querystring = {'tender_id': tender_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_tender_documents(123)

import requests
                
def list_notices():
    api_url = f"https://tenders.guru/api/es/notices"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_notices()

import requests
                
def get_notice_details(notice_id):
    api_url = f"https://tenders.guru/api/es/notices/{notice_id}"
    querystring = {'notice_id': notice_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_notice_details(456)

import requests
                
def get_notice_source_data(notice_id):
    api_url = f"https://tenders.guru/api/es/notices/{notice_id}/source_data"
    querystring = {'notice_id': notice_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_notice_source_data(456)

import requests
                
def list_notice_sections(notice_id):
    api_url = f"https://tenders.guru/api/es/notices/{notice_id}/sections"
    querystring = {'notice_id': notice_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_notice_sections(456)

import requests
                
def get_section_details(section_id):
    api_url = f"https://tenders.guru/api/es/sections/{section_id}"
    querystring = {'section_id': section_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_section_details(789)

import requests
                
def get_section_source_data(section_id):
    api_url = f"https://tenders.guru/api/es/sections/{section_id}/source_data"
    querystring = {'section_id': section_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_section_source_data(789)

