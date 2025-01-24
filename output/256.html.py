import requests
                
def query_recent_urls():
    api_url = f"https://urlhaus-api.abuse.ch/v1/urls/recent/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_recent_urls()

import requests
                
def query_recent_payloads():
    api_url = f"https://urlhaus-api.abuse.ch/v1/payloads/recent/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_recent_payloads()

import requests
                
def query_url_information(url):
    api_url = f"https://urlhaus-api.abuse.ch/v1/url/"
    payload = {'url': url, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_url_information('http://sskymedia.com/VMYB-ht_JAQo-gi/INV/99401FORPO/20673114777/US/Outstanding-Invoices/')

import requests
                
def query_url_information_by_id(id):
    api_url = f"https://urlhaus-api.abuse.ch/v1/urlid/"
    payload = {'id': id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_url_information_by_id('233833')

import requests
                
def query_host_information(host):
    api_url = f"https://urlhaus-api.abuse.ch/v1/host/"
    payload = {'host': host, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_host_information('vektorex.com')

import requests
                
def query_payload_information(md5_hash, sha256_hash):
    api_url = f"https://urlhaus-api.abuse.ch/v1/payload/"
    payload = {'md5_hash': md5_hash, 'sha256_hash': sha256_hash, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_payload_information('12c8aec5766ac3e6f26f2505e2f4a8f2', '0c415dd718e3b3728707d579cf8214f54c2942e964975a5f925e0b82fea644b4')

import requests
                
def query_tag_information(tag):
    api_url = f"https://urlhaus-api.abuse.ch/v1/tag/"
    payload = {'tag': tag, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_tag_information('Retefe')

import requests
                
def query_signature_information(signature):
    api_url = f"https://urlhaus-api.abuse.ch/v1/signature/"
    payload = {'signature': signature, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_signature_information('Gozi')

import requests
                
def download_malware_sample(sha256):
    api_url = f"https://urlhaus-api.abuse.ch/v1/download/{sha256}"
    querystring = {'sha256': sha256, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
download_malware_sample('254ca6a7a7ef7f17d9884c4a86f88b5d5fd8fe5341c0996eaaf1d4bcb3b2337b')

