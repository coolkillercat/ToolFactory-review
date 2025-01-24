import requests
                
def add_url(long):
    api_url = f"csclub.uwaterloo.ca/~phthakka/1pt-express"
    payload = {'long': long, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
add_url('https://www.param.me')

