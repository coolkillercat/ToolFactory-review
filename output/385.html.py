import requests
                
def retrieve_state_vectors(icao24, time):
    api_url = f"missing"
    querystring = {'icao24': icao24, 'time': time, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_state_vectors('c0ffee', 1458987225)

