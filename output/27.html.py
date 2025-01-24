import requests
                
def decode_vin(vin):
    api_url = f"/vehicles/DecodeVin/5UXWX7C5*BA?format=xml&modelyear=2011"
    querystring = {'vin': vin, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
decode_vin('5UXWX7C5*BA')

import requests
                
def decode_vin__flat_format_(vin):
    api_url = f"/vehicles/DecodeVinValues/5UXWX7C5*BA?format=xml&modelyear=2011"
    querystring = {'vin': vin, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
decode_vin__flat_format_('5UXWX7C5*BA')

import requests
                
def decode_vin_extended(vin):
    api_url = f"/vehicles/DecodeVinExtended/5UXWX7C5*BA?format=json&modelyear=2011"
    querystring = {'vin': vin, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
decode_vin_extended('5UXWX7C5*BA')

import requests
                
def decode_vin_extended__flat_format_(vin):
    api_url = f"/vehicles/DecodeVinValuesExtended/5UXWX7C5*BA?format=json&modelyear=2011"
    querystring = {'vin': vin, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
decode_vin_extended__flat_format_('5UXWX7C5*BA')

import requests
                
def decode_wmi(wmi):
    api_url = f"/vehicles/DecodeWMI/1FD?format=xml"
    querystring = {'wmi': wmi, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
decode_wmi('1FD')

import requests
                
def get_wmis_for_manufacturer(manufacturer):
    api_url = f"/vehicles/GetWMIsForManufacturer/hon?format=xml"
    querystring = {'manufacturer': manufacturer, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_wmis_for_manufacturer('hon')

import requests
                
def get_all_makes():
    api_url = f"/vehicles/GetAllMakes?format=csv"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_makes()

import requests
                
def get_parts(type):
    api_url = f"/vehicles/GetParts?type=565&fromDate=1/1/2015&toDate=5/5/2015&format=xml&page=1"
    querystring = {'type': type, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_parts(565)

import requests
                
def get_all_manufacturers():
    api_url = f"/vehicles/GetAllManufacturers?format=xml&page=2"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_manufacturers()

import requests
                
def get_manufacturer_details(manufacturer):
    api_url = f"/vehicles/GetManufacturerDetails/honda?format=xml"
    querystring = {'manufacturer': manufacturer, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_manufacturer_details('honda')

import requests
                
def get_makes_for_manufacturer_by_manufacturer_name(manufacturer):
    api_url = f"/vehicles/GetMakeForManufacturer/honda?format=json"
    querystring = {'manufacturer': manufacturer, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_makes_for_manufacturer_by_manufacturer_name('honda')

import requests
                
def get_makes_for_manufacturer_by_manufacturer_name_and_year(manufacturer, year):
    api_url = f"/vehicles/GetMakesForManufacturerAndYear/mer?year=2013&format=json"
    querystring = {'manufacturer': manufacturer, 'year': year, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_makes_for_manufacturer_by_manufacturer_name_and_year('mer', 2013)

import requests
                
def get_makes_for_vehicle_type_by_vehicle_type_name(vehicleType):
    api_url = f"/vehicles/GetMakesForVehicleType/car?format=json"
    querystring = {'vehicleType': vehicleType, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_makes_for_vehicle_type_by_vehicle_type_name('car')

import requests
                
def get_vehicle_types_for_make_by_name(make):
    api_url = f"/vehicles/GetVehicleTypesForMake/mercedes?format=json"
    querystring = {'make': make, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_vehicle_types_for_make_by_name('mercedes')

import requests
                
def get_vehicle_types_for_make_by_id(makeId):
    api_url = f"/vehicles/GetVehicleTypesForMakeId/450?format=json"
    querystring = {'makeId': makeId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_vehicle_types_for_make_by_id(450)

import requests
                
def get_equipment_plant_codes(year):
    api_url = f"/vehicles/GetEquipmentPlantCodes/2015?format=json"
    querystring = {'year': year, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_equipment_plant_codes(2015)

import requests
                
def get_models_for_make(make):
    api_url = f"/vehicles/GetModelsForMake/honda?format=json"
    querystring = {'make': make, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_models_for_make('honda')

import requests
                
def get_models_for_makeid(makeId):
    api_url = f"/vehicles/GetModelsForMakeId/440?format=json"
    querystring = {'makeId': makeId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_models_for_makeid(440)

import requests
                
def get_models_for_make_and_a_combination_of_year_and_vehicle_type(make):
    api_url = f"/vehicles/GetModelsForMakeYear/make/honda/modelyear/2015?format=csv"
    querystring = {'make': make, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_models_for_make_and_a_combination_of_year_and_vehicle_type('honda')

import requests
                
def get_models_for_make_id_and_a_combination_of_year_and_vehicle_type(makeId):
    api_url = f"/vehicles/GetModelsForMakeIdYear/makeId/474/modelyear/2015?format=csv"
    querystring = {'makeId': makeId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_models_for_make_id_and_a_combination_of_year_and_vehicle_type(None)

