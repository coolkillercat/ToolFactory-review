import requests
                
def get_weather_by_city(city):
    api_url = f"https://goweather.herokuapp.com/weather/{city}"
    querystring = {'city': city, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_weather_by_city('Curitiba')

