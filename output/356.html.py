import requests
                
def get_carbon_intensity___national():
    api_url = f"https://api.carbonintensity.org.uk/intensity"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity___national()

import requests
                
def get_carbon_intensity_by_date():
    api_url = f"https://api.carbonintensity.org.uk/intensity/date"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_by_date()

import requests
                
def get_carbon_intensity_by_specific_date(date):
    api_url = f"https://api.carbonintensity.org.uk/intensity/date/{date}"
    querystring = {'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_by_specific_date('2017-08-25')

import requests
                
def get_carbon_intensity_by_date_and_period(date, period):
    api_url = f"https://api.carbonintensity.org.uk/intensity/date/{date}/{period}"
    querystring = {'date': date, 'period': period, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_by_date_and_period('2017-08-25', '42')

import requests
                
def get_carbon_intensity_factors():
    api_url = f"https://api.carbonintensity.org.uk/intensity/factors"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_factors()

import requests
                
def get_carbon_intensity_by_from_date(from):
    api_url = f"https://api.carbonintensity.org.uk/intensity/{from}"
    querystring = {'from': from, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_by_from_date('2017-08-25T12:35Z')

import requests
                
def get_carbon_intensity_24hrs_forward(from):
    api_url = f"https://api.carbonintensity.org.uk/intensity/{from}/fw24h"
    querystring = {'from': from, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_24hrs_forward('2017-08-25T12:35Z')

import requests
                
def get_carbon_intensity_48hrs_forward(from):
    api_url = f"https://api.carbonintensity.org.uk/intensity/{from}/fw48h"
    querystring = {'from': from, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_48hrs_forward('2017-08-25T12:35Z')

import requests
                
def get_carbon_intensity_24hrs_past(from):
    api_url = f"https://api.carbonintensity.org.uk/intensity/{from}/pt24h"
    querystring = {'from': from, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_24hrs_past('2017-08-25T12:35Z')

import requests
                
def get_carbon_intensity_between_dates(from, to):
    api_url = f"https://api.carbonintensity.org.uk/intensity/{from}/{to}"
    querystring = {'from': from, 'to': to, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_between_dates('2017-08-25T12:35Z', '2017-08-26T12:35Z')

import requests
                
def get_carbon_intensity_statistics(from, to):
    api_url = f"https://api.carbonintensity.org.uk/intensity/stats/{from}/{to}"
    querystring = {'from': from, 'to': to, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_carbon_intensity_statistics('2017-08-25T12:35Z', '2017-08-26T12:35Z')

import requests
                
def get_block_average_carbon_intensity_statistics(from, to, block):
    api_url = f"https://api.carbonintensity.org.uk/intensity/stats/{from}/{to}/{block}"
    querystring = {'from': from, 'to': to, 'block': block, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_block_average_carbon_intensity_statistics('2017-08-25T12:35Z', '2017-08-26T12:35Z', '2')

import requests
                
def get_generation_mix():
    api_url = f"https://api.carbonintensity.org.uk/generation"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_generation_mix()

import requests
                
def get_generation_mix_for_past_24_hours(from):
    api_url = f"https://api.carbonintensity.org.uk/generation/{from}/pt24h"
    querystring = {'from': from, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_generation_mix_for_past_24_hours('2017-08-25T12:35Z')

import requests
                
def get_generation_mix_between_dates(from, to):
    api_url = f"https://api.carbonintensity.org.uk/generation/{from}/{to}"
    querystring = {'from': from, 'to': to, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_generation_mix_between_dates('2017-08-25T12:35Z', '2017-08-26T12:35Z')

import requests
                
def get_regional_carbon_intensity():
    api_url = f"https://api.carbonintensity.org.uk/regional"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity()

import requests
                
def get_regional_carbon_intensity_for_england():
    api_url = f"https://api.carbonintensity.org.uk/regional/england"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_for_england()

import requests
                
def get_regional_carbon_intensity_for_scotland():
    api_url = f"https://api.carbonintensity.org.uk/regional/scotland"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_for_scotland()

import requests
                
def get_regional_carbon_intensity_for_wales():
    api_url = f"https://api.carbonintensity.org.uk/regional/wales"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_for_wales()

import requests
                
def get_regional_carbon_intensity_by_postcode(postcode):
    api_url = f"https://api.carbonintensity.org.uk/regional/postcode/{postcode}"
    querystring = {'postcode': postcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_by_postcode('RG41')

import requests
                
def get_regional_carbon_intensity_by_region_id(regionid):
    api_url = f"https://api.carbonintensity.org.uk/regional/regionid/{regionid}"
    querystring = {'regionid': regionid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_by_region_id('3')

import requests
                
def get_regional_carbon_intensity_for_next_24h(from):
    api_url = f"https://api.carbonintensity.org.uk/regional/intensity/{from}/fw24h"
    querystring = {'from': from, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_for_next_24h('2017-08-25T12:35Z')

import requests
                
def get_regional_carbon_intensity_for_next_24h_by_postcode(from, postcode):
    api_url = f"https://api.carbonintensity.org.uk/regional/intensity/{from}/fw24h/postcode/{postcode}"
    querystring = {'from': from, 'postcode': postcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_for_next_24h_by_postcode('2017-08-25T12:35Z', 'RG41')

import requests
                
def get_regional_carbon_intensity_for_next_24h_by_region_id(from, regionid):
    api_url = f"https://api.carbonintensity.org.uk/regional/intensity/{from}/fw24h/regionid/{regionid}"
    querystring = {'from': from, 'regionid': regionid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_for_next_24h_by_region_id('2017-08-25T12:35Z', '3')

import requests
                
def get_regional_carbon_intensity_for_next_48h(from):
    api_url = f"https://api.carbonintensity.org.uk/regional/intensity/{from}/fw48h"
    querystring = {'from': from, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_for_next_48h('2017-08-25T12:35Z')

import requests
                
def get_regional_carbon_intensity_for_next_48h_by_postcode(from, postcode):
    api_url = f"https://api.carbonintensity.org.uk/regional/intensity/{from}/fw48h/postcode/{postcode}"
    querystring = {'from': from, 'postcode': postcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_regional_carbon_intensity_for_next_48h_by_postcode('2017-08-25T12:35Z', 'RG41')

