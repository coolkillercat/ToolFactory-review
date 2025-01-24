import requests
                
def escape_html(method, data):
    api_url = f"https://s.polarspetroll.repl.co/api"
    querystring = {'method': method, 'data': data, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
escape_html('html', '<>/>,test'')

import requests
                
def escape_shell(method, data):
    api_url = f"https://s.polarspetroll.repl.co/api"
    querystring = {'method': method, 'data': data, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
escape_shell('shell', 'ls -la | cat /etc/passwd')

import requests
                
def escape_path(method, data):
    api_url = f"https://s.polarspetroll.repl.co/api"
    querystring = {'method': method, 'data': data, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
escape_path('path', '../../../../../../../etc/passwd')

