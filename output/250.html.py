import requests
                
def list_all_asteroids():
    api_url = f"http://asterank.com/api/mpc"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_all_asteroids()

