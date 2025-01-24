import requests
                
def retorna_moedas_selecionadas(moedas):
    api_url = f"https://economia.awesomeapi.com.br/json/last/:moedas"
    querystring = {'moedas': moedas, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retorna_moedas_selecionadas('USD-BRL,EUR-BRL,BTC-BRL')

import requests
                
def retorna_o_fechamento_dos_últimos_dias(moeda, numero_dias):
    api_url = f"https://economia.awesomeapi.com.br/json/daily/:moeda/:numero_dias"
    querystring = {'moeda': moeda, 'numero_dias': numero_dias, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retorna_o_fechamento_dos_últimos_dias('USD-BRL', 15)

import requests
                
def retorna_o_fechamento_de_um_período_específico(moeda):
    api_url = f"https://economia.awesomeapi.com.br/json/daily/:moeda?start_date=YYYYMMDD&end_date=YYYYMMDD"
    querystring = {'moeda': moeda, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retorna_o_fechamento_de_um_período_específico('USD-BRL')

import requests
                
def retorna_cotações_sequenciais_de_uma_única_moeda(moeda, quantidade):
    api_url = f"https://economia.awesomeapi.com.br/:moeda/:quantidade"
    querystring = {'moeda': moeda, 'quantidade': quantidade, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retorna_cotações_sequenciais_de_uma_única_moeda('USD-BRL', 10)

import requests
                
def retorna_cotações_sequenciais_de_um_período_específico(moeda, quantidade):
    api_url = f"https://economia.awesomeapi.com.br/:moeda/:quantidade?start_date=YYYYMMDD&end_date=YYYYMMDD"
    querystring = {'moeda': moeda, 'quantidade': quantidade, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retorna_cotações_sequenciais_de_um_período_específico('USD-BRL', 10)

import requests
                
def formato_de_resposta(format, moeda):
    api_url = f"https://economia.awesomeapi.com.br/:format/:moeda"
    querystring = {'format': format, 'moeda': moeda, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
formato_de_resposta('json', 'USD-BRL')

