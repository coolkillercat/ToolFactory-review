import requests
                
def generate_random_password():
    api_url = f"https://passwordinator.onrender.com"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_random_password()

