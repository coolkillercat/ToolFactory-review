import requests
                
def bin_iin_lookup(bin):
    api_url = f"https://lookup.binlist.net/{bin}"
    querystring = {'bin': bin, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
bin_iin_lookup('45717360')

