import requests
                
def lookup_icelandic_addresses(address):
    api_url = f"http://apis.is/address"
    querystring = {'address': address, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lookup_icelandic_addresses('laugavegur 1')

import requests
                
def real_time_bus_locations():
    api_url = f"http://apis.is/bus/realtime"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
real_time_bus_locations()

import requests
                
def search_icelandic_vehicle_registry(number):
    api_url = f"http://apis.is/car"
    querystring = {'number': number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_icelandic_vehicle_registry('aa031')

import requests
                
def search_icelandic_company_registry():
    api_url = f"http://apis.is/company"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_icelandic_company_registry()

import requests
                
def list_of_concerts_in_iceland():
    api_url = f"http://apis.is/concerts"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_of_concerts_in_iceland()

import requests
                
def get_currency_data(source):
    api_url = f"http://apis.is/currency/:source"
    querystring = {'source': source, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_currency_data('m5')

import requests
                
def get_bicycle_counter_status():
    api_url = f"http://apis.is/cyclecounter"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_bicycle_counter_status()

import requests
                
def get_earthquake_data():
    api_url = f"http://apis.is/earthquake/is"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_earthquake_data()

import requests
                
def get_international_flights():
    api_url = f"http://apis.is/flight"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_international_flights()

import requests
                
def get_hospital_status():
    api_url = f"http://apis.is/hospital"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_hospital_status()

import requests
                
def get_icelandic_lottery_numbers():
    api_url = f"http://apis.is/lottery"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_icelandic_lottery_numbers()

import requests
                
def get_vikingalotto_numbers():
    api_url = f"http://apis.is/lottery/vikingalotto"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_vikingalotto_numbers()

import requests
                
def get_eurojackpot_numbers():
    api_url = f"http://apis.is/lottery/eurojackpot"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_eurojackpot_numbers()

import requests
                
def get_particulates_status():
    api_url = f"http://apis.is/particulates"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_particulates_status()

import requests
                
def get_carpooling_drivers():
    api_url = f"http://apis.is/rides/samferda-drivers/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carpooling_drivers()

import requests
                
def get_carpooling_passengers():
    api_url = f"http://apis.is/rides/samferda-passengers/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carpooling_passengers()

import requests
                
def get_sar_school_courses():
    api_url = f"http://apis.is/sarschool"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sar_school_courses()

import requests
                
def get_sports_events(sport):
    api_url = f"http://apis.is/sports/:sport"
    querystring = {'sport': sport, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sports_events('football')

import requests
                
def get_tv_schedules(channel):
    api_url = f"http://apis.is/tv/:channel"
    querystring = {'channel': channel, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_tv_schedules('ruv')

import requests
                
def get_weather_information(type, lang):
    api_url = f"http://apis.is/weather/:type/:lang"
    querystring = {'type': type, 'lang': 'is', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_weather_information('forecasts', 'en')

import requests
                
def search_icelandic_horse_database():
    api_url = f"http://apis.is/horses"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_icelandic_horse_database()

import requests
                
def get_petrol_stations():
    api_url = f"http://apis.is/petrol"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_petrol_stations()

import requests
                
def get_auroracoin_exchange_rate():
    api_url = f"http://apis.is/aur"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_auroracoin_exchange_rate()

import requests
                
def get_auroracoin_exchange_rate_history():
    api_url = f"http://apis.is/aur/history"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_auroracoin_exchange_rate_history()

import requests
                
def get_auroracoin_transactions():
    api_url = f"http://apis.is/aur/transactions"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_auroracoin_transactions()

import requests
                
def get_auroracoin_order_book():
    api_url = f"http://apis.is/aur/order-book"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_auroracoin_order_book()

import requests
                
def search_icelandic_ship_registry(search):
    api_url = f"http://apis.is/ship"
    querystring = {'search': search, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_icelandic_ship_registry('engey')

