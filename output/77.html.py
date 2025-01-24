import requests
                
def invoke_assessment(host):
    api_url = f"https://http-observatory.security.mozilla.org/api/v1/analyze"
    payload = {'host': host, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
invoke_assessment('www.mozilla.org')

import requests
                
def retrieve_assessment(host):
    api_url = f"https://http-observatory.security.mozilla.org/api/v1/analyze"
    querystring = {'host': host, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_assessment('www.mozilla.org')

import requests
                
def retrieve_test_results(scan):
    api_url = f"https://http-observatory.security.mozilla.org/api/v1/getScanResults"
    querystring = {'scan': scan, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_test_results(123456)

import requests
                
def retrieve_recent_scans():
    api_url = f"https://http-observatory.security.mozilla.org/api/v1/getRecentScans"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_recent_scans()

import requests
                
def retrieve_host_s_scan_history(host):
    api_url = f"https://http-observatory.security.mozilla.org/api/v1/getHostHistory"
    querystring = {'host': host, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_host_s_scan_history('mozilla.org')

import requests
                
def retrieve_overall_grade_distribution():
    api_url = f"https://http-observatory.security.mozilla.org/api/v1/getGradeDistribution"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_overall_grade_distribution()

import requests
                
def retrieve_scanner_states__deprecated_():
    api_url = f"https://http-observatory.security.mozilla.org/api/v1/getScannerStates"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_scanner_states__deprecated_()

