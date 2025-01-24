import requests
                
def get_server_status(address):
    api_url = f"https://api.mcsrvstat.us/3/{address}"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_server_status('play.example.com')

import requests
                
def get_bedrock_server_status(address):
    api_url = f"https://api.mcsrvstat.us/bedrock/3/{address}"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_bedrock_server_status('play.example.com')

import requests
                
def http_status_code_endpoint(address):
    api_url = f"https://api.mcsrvstat.us/simple/{address}"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
http_status_code_endpoint('play.example.com')

import requests
                
def http_status_code_endpoint_for_bedrock(address):
    api_url = f"https://api.mcsrvstat.us/bedrock/simple/{address}"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
http_status_code_endpoint_for_bedrock('play.example.com')

import requests
                
def get_server_icon(address):
    api_url = f"https://api.mcsrvstat.us/icon/{address}"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_server_icon('play.example.com')

import requests
                
def debug_ping(address):
    api_url = f"https://api.mcsrvstat.us/debug/ping/{address}"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
debug_ping('play.example.com')

import requests
                
def debug_query(address):
    api_url = f"https://api.mcsrvstat.us/debug/query/{address}"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
debug_query('play.example.com')

import requests
                
def debug_bedrock(address):
    api_url = f"https://api.mcsrvstat.us/debug/bedrock/{address}"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
debug_bedrock('play.example.com')

