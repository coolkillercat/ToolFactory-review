import requests
                
def generate_version_1_uuid():
    api_url = f"https://www.uuidtools.com/api/generate/v1"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_version_1_uuid()

import requests
                
def generate_multiple_version_1_uuids():
    api_url = f"https://www.uuidtools.com/api/generate/v1/count/10"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_multiple_version_1_uuids()

import requests
                
def generate_version_3_uuid(namespace, name):
    api_url = f"https://www.uuidtools.com/api/generate/v3/namespace/ns:url/name/https://www.google.com/"
    querystring = {'namespace': namespace, 'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_version_3_uuid('ns:url', 'https://www.google.com/')

import requests
                
def generate_version_4_uuid():
    api_url = f"https://www.uuidtools.com/api/generate/v4"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_version_4_uuid()

import requests
                
def generate_multiple_version_4_uuids():
    api_url = f"https://www.uuidtools.com/api/generate/v4/count/10"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_multiple_version_4_uuids()

import requests
                
def generate_version_5_uuid(namespace, name):
    api_url = f"https://www.uuidtools.com/api/generate/v5/namespace/ns:url/name/https://www.uuidtools.com/generate"
    querystring = {'namespace': namespace, 'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_version_5_uuid('ns:url', 'https://www.uuidtools.com/generate')

import requests
                
def generate_timestamp_first_uuid():
    api_url = f"https://www.uuidtools.com/api/generate/timestamp-first"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_timestamp_first_uuid()

import requests
                
def generate_multiple_timestamp_first_uuids():
    api_url = f"https://www.uuidtools.com/api/generate/timestamp-first/count/10"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_multiple_timestamp_first_uuids()

import requests
                
def decode_uuid(uuid):
    api_url = f"https://www.uuidtools.com/api/decode/b01eb720-171a-11ea-b949-73c91bba743d"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
decode_uuid('b01eb720-171a-11ea-b949-73c91bba743d')

