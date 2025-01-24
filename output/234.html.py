import requests
                
def get_trace_information():
    api_url = f"https://one.one.one.one/cdn-cgi/trace"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_trace_information()

