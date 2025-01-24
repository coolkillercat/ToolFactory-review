import requests
                
def get_product_data(barcode):
    api_url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
    querystring = {'barcode': barcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_product_data('737628064502')

import requests
                
def get_product_data__xml_(barcode):
    api_url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.xml"
    querystring = {'barcode': barcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_product_data__xml_('737628064502')

import requests
                
def get_delta_export(filename):
    api_url = f"https://static.openfoodfacts.org/data/delta/{filename}"
    querystring = {'filename': filename, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_delta_export('delta_1609459200_1609545600.json')

import requests
                
def get_mongodb_dump():
    api_url = f"https://static.openfoodfacts.org/data/openfoodfacts-mongodbdump.gz"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_mongodb_dump()

import requests
                
def get_jsonl_data_export():
    api_url = f"https://static.openfoodfacts.org/data/openfoodfacts-products.jsonl.gz"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_jsonl_data_export()

import requests
                
def get_csv_data_export():
    api_url = f"https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_csv_data_export()

import requests
                
def get_rdf_data_export():
    api_url = f"https://world.openfoodfacts.org/data/en.openfoodfacts.org.products.rdf.gz"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_rdf_data_export()

