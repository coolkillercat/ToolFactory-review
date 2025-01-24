import requests
                
def get_bank_details_using_ifsc(ifsc):
    api_url = f"https://bank-apis.justinclicks.com/api/v1/getBankDetails"
    querystring = {'ifsc': ifsc, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_bank_details_using_ifsc('SBIN0000001')

import requests
                
def get_data_by_selections():
    api_url = f"https://bank-apis.justinclicks.com/api/v1/getDataBySelections"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_data_by_selections()

import requests
                
def get_excel_file_of_any_bank(bank_name):
    api_url = f"https://bank-apis.justinclicks.com/api/v1/getExcelFile"
    querystring = {'bank_name': bank_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_excel_file_of_any_bank('State Bank of India')

import requests
                
def api_status():
    api_url = f"https://bank-apis.justinclicks.com/api/v1/status"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
api_status()

