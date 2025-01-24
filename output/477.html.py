import requests
                
def get_sunset_and_sunrise_times(lat, lng):
    api_url = f"https://api.sunrise-sunset.org/json"
    querystring = {'lat': lat, 'lng': lng, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sunset_and_sunrise_times(36.72016, -4.42034)

