import requests
                
def predict_nationality_from_a_name(name):
    api_url = f"https://api.nationalize.io"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
predict_nationality_from_a_name('John')

