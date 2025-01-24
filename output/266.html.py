import requests
                
def calculate_expression(query):
    api_url = f"https://remote-calc.herokuapp.com/calculus?query=[input]"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
calculate_expression('MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk')

