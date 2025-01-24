import requests
                
def graphical_api(lon, lat):
    api_url = f"http://www.7timer.info/bin/astro.php?lon=113.17&lat=23.09&ac=0&lang=en&unit=metric&output=internal&tzshift=0"
    querystring = {'lon': lon, 'lat': lat, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
graphical_api(113.17, 23.09)

import requests
                
def machine_readable_api(lon, lat, product, output):
    api_url = f"http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=xml"
    querystring = {'lon': lon, 'lat': lat, 'product': product, 'output': output, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
machine_readable_api(113.17, 23.09, 'astro', 'xml')

