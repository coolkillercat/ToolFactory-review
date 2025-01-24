import requests
                
def consultar_cep(cep_a_consultar):
    api_url = f"https://api.postmon.com.br/v1/cep/{cep_a_consultar}"
    querystring = {'cep_a_consultar': cep_a_consultar, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
consultar_cep('01001-000')

import requests
                
def consultar_encomenda(provider, codigo_rastreio):
    api_url = f"https://api.postmon.com.br/v1/rastreio/{provider}/{codigo_rastreio}"
    querystring = {'provider': provider, 'codigo_rastreio': codigo_rastreio, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
consultar_encomenda('ect', 'AB123456789BR')

