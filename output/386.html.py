import requests
                
def query_by_id(ids, fields):
    api_url = f"http://libgen.io/json.php"
    querystring = {'ids': ids, 'fields': fields, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query_by_id('1,2', 'Title,Author,MD5')

import requests
                
def search_by_date(mode, timefirst):
    api_url = f"http://libgen.io/json.php"
    querystring = {'mode': mode, 'timefirst': timefirst, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_by_date('last', '2013-05-01')

import requests
                
def incremental_updates(mode, timenewer, idnewer):
    api_url = f"http://libgen.io/json.php"
    querystring = {'mode': mode, 'timenewer': timenewer, 'idnewer': idnewer, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
incremental_updates('newer', '2014-01-01%2000:00:00', 1)

