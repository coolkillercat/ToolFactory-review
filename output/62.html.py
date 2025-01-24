import requests
                
def get_ip_geolocation(ip):
    api_url = f"missing"
    querystring = {'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_ip_geolocation('203.91.85.36')

