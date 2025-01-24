import requests
                
def get_recordings(query):
    api_url = f"https://xeno-canto.org/api/2/recordings"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_recordings('cnt:brazil')

