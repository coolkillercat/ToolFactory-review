import requests
                
def example_endpoint(exampleParam):
    api_url = f"missing"
    querystring = {'exampleParam': exampleParam, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
example_endpoint('exampleValue')

