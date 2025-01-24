import requests
                
def convert_json_to_jsonp(url, callback):
    api_url = f"https://json2jsonp.com/"
    querystring = {'url': url, 'callback': callback, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
convert_json_to_jsonp('http://domain.com/some/json', 'cbfunc')

