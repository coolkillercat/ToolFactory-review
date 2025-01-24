import requests
                
def get_phishing_data_by_id(id):
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(id,eq,{id})"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_id(3296584)

import requests
                
def get_phishing_data_by_asn(asn):
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(asn,eq,{asn})"
    querystring = {'asn': asn, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_asn('as14061')

import requests
                
def get_phishing_data_by_ip(ip):
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(ip,eq,{ip})"
    querystring = {'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_ip('148.228.16.3')

import requests
                
def get_phishing_data_by_country_code(countrycode):
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(countrycode,eq,{countrycode})"
    querystring = {'countrycode': countrycode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_country_code('US')

import requests
                
def get_phishing_data_by_tld(tld):
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(tld,eq,{tld})"
    querystring = {'tld': tld, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_tld('US')

import requests
                
def get_phishing_data_sorted_by_id():
    api_url = f"https://phishstats.info:2096/api/phishing?_sort=-id"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_sorted_by_id()

import requests
                
def get_phishing_data_sorted_by_date():
    api_url = f"https://phishstats.info:2096/api/phishing?_sort=-date"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_sorted_by_date()

import requests
                
def get_phishing_data_by_title_with_id_sorted(title):
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(title,like,~{title}~)&_sort=-id"
    querystring = {'title': title, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_title_with_id_sorted('apple')

import requests
                
def get_phishing_data_by_url_with_id_sorted(url):
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(url,like,~{url}~)&_sort=-id"
    querystring = {'url': url, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_url_with_id_sorted('apple')

import requests
                
def get_phishing_data_by_title_or_url_with_id_sorted(title, url):
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(title,like,~{title}~)~or(url,like,~{url}~)&_sort=-id"
    querystring = {'title': title, 'url': url, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_title_or_url_with_id_sorted('apple', 'apple')

import requests
                
def get_phishing_data_by_score_and_tld():
    api_url = f"https://phishstats.info:2096/api/phishing?_where=(score,gt,5)~and(tld,eq,br)~and(countrycode,ne,br)&_sort=-id"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_phishing_data_by_score_and_tld()

