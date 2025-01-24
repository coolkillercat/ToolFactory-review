import requests
                
def despesas_pela_cota_para_exercício_da_atividade_parlamentar(ano, formato):
    api_url = f"http://www.camara.leg.br/cotas/Ano-{ano}.{formato}[.zip]"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
despesas_pela_cota_para_exercício_da_atividade_parlamentar(2023, 'json')

import requests
                
def proposições(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/proposicoes/{formato}/proposicoes-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
proposições(2023, 'json')

import requests
                
def classificação_temática_das_proposições(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/proposicoesTemas/{formato}/proposicoesTemas-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
classificação_temática_das_proposições(2023, 'json')

import requests
                
def autores_das_proposições(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/{formato}/proposicoesAutores-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
autores_das_proposições(2023, 'json')

import requests
                
def frentes_parlamentares(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/frentes/{formato}/frentes.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
frentes_parlamentares('json')

import requests
                
def deputados_das_frentes(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/frentesDeputados/{formato}/frentesDeputados.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
deputados_das_frentes('json')

import requests
                
def grupos_parlamentares(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/grupos/{formato}/grupos.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
grupos_parlamentares('json')

import requests
                
def membros_dos_grupos_parlamentares(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/gruposMembros/{formato}/gruposMembros.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
membros_dos_grupos_parlamentares('json')

import requests
                
def histórico_dos_grupos_parlamentares(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/gruposHistorico/{formato}/gruposHistorico.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
histórico_dos_grupos_parlamentares('json')

import requests
                
def legislaturas(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/legislaturas/{formato}/legislaturas.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
legislaturas('json')

import requests
                
def mesas_diretoras(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/legislaturasMesas/{formato}/legislaturasMesas.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
mesas_diretoras('json')

import requests
                
def órgãos_da_câmara(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/orgaos/{formato}/orgaos.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
órgãos_da_câmara('json')

import requests
                
def deputados_membros_dos_órgãos(legislatura, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/orgaosDeputados/{formato}/orgaosDeputados-L{legislatura}.{formato}"
    querystring = {'legislatura': legislatura, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
deputados_membros_dos_órgãos(54, 'json')

import requests
                
def deputados(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/deputados/{formato}/deputados.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
deputados('json')

import requests
                
def ocupações_dos_deputados(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/deputadosOcupacoes/{formato}/deputadosOcupacoes.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
ocupações_dos_deputados('json')

import requests
                
def profissões_dos_deputados(formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/deputadosProfissoes/{formato}/deputadosProfissoes.{formato}"
    querystring = {'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
profissões_dos_deputados('json')

import requests
                
def eventos(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/eventos/{formato}/eventos-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
eventos(2023, 'json')

import requests
                
def eventos_e_seus_órgãos_realizadores(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/eventosOrgaos/{formato}/eventosOrgaos-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
eventos_e_seus_órgãos_realizadores(2023, 'json')

import requests
                
def deputados_presentes_em_cada_evento(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/eventosPresencaDeputados/{formato}/eventosPresencaDeputados-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
deputados_presentes_em_cada_evento(2023, 'json')

import requests
                
def requerimentos_de_realização_de_eventos(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/eventosRequerimentos/{formato}/eventosRequerimentos-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
requerimentos_de_realização_de_eventos(2023, 'json')

import requests
                
def votações_realizadas_a_cada_ano(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/votacoes/{formato}/votacoes-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
votações_realizadas_a_cada_ano(2023, 'json')

import requests
                
def orientações_de_bancadas_por_votação(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/votacoesOrientacoes/{formato}/votacoesOrientacoes-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
orientações_de_bancadas_por_votação(2023, 'json')

import requests
                
def voto_de_cada_parlamentar(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/votacoesVotos/{formato}/votacoesVotos-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
voto_de_cada_parlamentar(2023, 'json')

import requests
                
def proposição_objeto_de_cada_votação(ano, formato):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/votacoesObjetos/{formato}/votacoesObjetos-{ano}.{formato}"
    querystring = {'ano': ano, 'formato': formato, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
proposição_objeto_de_cada_votação(2023, 'json')

import requests
                
def proposições_afetadas_por_votação(ano):
    api_url = f"http://dadosabertos.camara.leg.br/arquivos/votacoesProposicoes/{formato}/votacoesProposicoes-{ano}.{formato}"
    querystring = {'ano': ano, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
proposições_afetadas_por_votação(None)

