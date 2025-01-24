import requests
                
def list_brands():
    api_url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_brands()

import requests
                
def list_models(brandId):
    api_url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{brandId}/modelos"
    querystring = {'brandId': brandId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_models('59')

import requests
                
def list_years(brandId, modelId):
    api_url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{brandId}/modelos/{modelId}/anos"
    querystring = {'brandId': brandId, 'modelId': modelId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_years('59', '5940')

import requests
                
def get_vehicle_price(brandId, modelId, yearId):
    api_url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{brandId}/modelos/{modelId}/anos/{yearId}"
    querystring = {'brandId': brandId, 'modelId': modelId, 'yearId': yearId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_vehicle_price('59', '5940', '2014-3')

