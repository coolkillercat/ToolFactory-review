import requests
                
def neighbourhood_team_members():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
neighbourhood_team_members()

import requests
                
def upcoming_events():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
upcoming_events()

import requests
                
def street_level_crime_and_outcome_data():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
street_level_crime_and_outcome_data()

import requests
                
def nearest_police_stations():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
nearest_police_stations()

import requests
                
def forces():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
forces()

import requests
                
def specific_force(forceId):
    api_url = f"missing"
    querystring = {'forceId': forceId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
specific_force('leicestershire')

import requests
                
def force_senior_officers(forceId):
    api_url = f"missing"
    querystring = {'forceId': forceId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
force_senior_officers('leicestershire')

import requests
                
def street_level_crimes(lat, lng):
    api_url = f"missing"
    querystring = {'lat': lat, 'lng': lng, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
street_level_crimes(52.629729, -1.131592)

import requests
                
def street_level_outcomes(lat, lng):
    api_url = f"missing"
    querystring = {'lat': lat, 'lng': lng, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
street_level_outcomes(52.629729, -1.131592)

import requests
                
def crimes_at_location(locationId):
    api_url = f"missing"
    querystring = {'locationId': locationId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
crimes_at_location('884227')

import requests
                
def crimes_with_no_location():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
crimes_with_no_location()

import requests
                
def crime_categories():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
crime_categories()

import requests
                
def outcomes_for_a_specific_crime(crimeId):
    api_url = f"missing"
    querystring = {'crimeId': crimeId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
outcomes_for_a_specific_crime('12345678')

import requests
                
def neighbourhoods():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
neighbourhoods()

import requests
                
def specific_neighbourhood(neighbourhoodId):
    api_url = f"missing"
    querystring = {'neighbourhoodId': neighbourhoodId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
specific_neighbourhood('E05001895')

import requests
                
def neighbourhood_boundary(neighbourhoodId):
    api_url = f"missing"
    querystring = {'neighbourhoodId': neighbourhoodId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
neighbourhood_boundary('E05001895')

import requests
                
def neighbourhood_team(neighbourhoodId):
    api_url = f"missing"
    querystring = {'neighbourhoodId': neighbourhoodId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
neighbourhood_team('E05001895')

import requests
                
def neighbourhood_events(neighbourhoodId):
    api_url = f"missing"
    querystring = {'neighbourhoodId': neighbourhoodId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
neighbourhood_events('E05001895')

import requests
                
def neighbourhood_priorities(neighbourhoodId):
    api_url = f"missing"
    querystring = {'neighbourhoodId': neighbourhoodId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
neighbourhood_priorities('E05001895')

import requests
                
def locate_neighbourhood(lat, lng):
    api_url = f"missing"
    querystring = {'lat': lat, 'lng': lng, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
locate_neighbourhood(52.629729, -1.131592)

import requests
                
def stop_and_searches_by_area(lat, lng):
    api_url = f"missing"
    querystring = {'lat': lat, 'lng': lng, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
stop_and_searches_by_area(52.629729, -1.131592)

import requests
                
def stop_and_searches_by_location(locationId):
    api_url = f"missing"
    querystring = {'locationId': locationId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
stop_and_searches_by_location('884227')

import requests
                
def stop_and_searches_with_no_location():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
stop_and_searches_with_no_location()

import requests
                
def stop_and_searches_by_force(forceId):
    api_url = f"missing"
    querystring = {'forceId': forceId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
stop_and_searches_by_force('leicestershire')

