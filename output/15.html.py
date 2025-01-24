import requests
                
def search_registered_domain_names(domain):
    api_url = f"https://api.domainsdb.info/v1/domains/search?domain={query}"
    querystring = {'domain': domain, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_registered_domain_names('facebook')

