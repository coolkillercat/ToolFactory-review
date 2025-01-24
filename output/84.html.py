import requests
                
def get_postal_code_information(country, postal_code):
    api_url = f"http://api.zippopotam.us/{country}/{postal-code}"
    querystring = {'country': country, 'postal_code': postal_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_postal_code_information('us', '90210')

import requests
                
def get_city_information(country, state, city):
    api_url = f"http://api.zippopotam.us/{country}/{state}/{city}"
    querystring = {'country': country, 'state': state, 'city': city, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_city_information('us', 'ma', 'belmont')

