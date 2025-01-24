import requests
                
def lookup_entity(ENTITY_TYPE, MBID):
    api_url = f"https://musicbrainz.org/ws/2/{ENTITY_TYPE}/{MBID}?inc={INC}"
    querystring = {'ENTITY_TYPE': ENTITY_TYPE, 'MBID': MBID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
lookup_entity('artist', '65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab')

import requests
                
def search_entity(ENTITY_TYPE, QUERY):
    api_url = f"https://musicbrainz.org/ws/2/{ENTITY_TYPE}?query={QUERY}&limit={LIMIT}&offset={OFFSET}"
    querystring = {'ENTITY_TYPE': ENTITY_TYPE, 'QUERY': QUERY, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_entity('artist', 'Beatles')

import requests
                
def browse_entity(RESULT_ENTITY_TYPE, BROWSING_ENTITY_TYPE, MBID):
    api_url = f"https://musicbrainz.org/ws/2/{RESULT_ENTITY_TYPE}?{BROWSING_ENTITY_TYPE}={MBID}&limit={LIMIT}&offset={OFFSET}&inc={INC}"
    querystring = {'RESULT_ENTITY_TYPE': RESULT_ENTITY_TYPE, 'BROWSING_ENTITY_TYPE': BROWSING_ENTITY_TYPE, 'MBID': MBID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
browse_entity('release', 'artist', '65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab')

import requests
                
def submit_tags(CLIENT):
    api_url = f"https://musicbrainz.org/ws/2/tag?client={CLIENT}"
    payload = {'CLIENT': CLIENT, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
submit_tags('example.app-0.4.7')

import requests
                
def submit_ratings(CLIENT):
    api_url = f"https://musicbrainz.org/ws/2/rating?client={CLIENT}"
    payload = {'CLIENT': CLIENT, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
submit_ratings('example.app-0.4.7')

import requests
                
def submit_barcode(CLIENT):
    api_url = f"https://musicbrainz.org/ws/2/release/?client={CLIENT}"
    payload = {'CLIENT': CLIENT, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
submit_barcode('example.app-0.4.7')

import requests
                
def submit_isrc(CLIENT):
    api_url = f"https://musicbrainz.org/ws/2/recording/?client={CLIENT}"
    payload = {'CLIENT': CLIENT, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
submit_isrc('example.app-0.4.7')

