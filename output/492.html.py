import requests
                
def validate_ip_address(ip):
    api_url = f"https://googlebot.seoapi.com/v1/validate/?ip=IPADDRESS"
    querystring = {'ip': ip, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
validate_ip_address('66.249.66.160')

