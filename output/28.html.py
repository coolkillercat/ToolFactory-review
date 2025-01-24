import requests
                
def point_query(locations):
    api_url = f"https://api.opentopodata.org/v1/test-dataset"
    querystring = {'locations': locations, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
point_query('56.35,123.90')

