import requests
                
def получение_котировок_на_заданный_день():
    api_url = f"http://www.cbr.ru/scripts/XML_daily.asp"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_котировок_на_заданный_день()

import requests
                
def получение_динамики_котировок_доллара_сша(date_req1, date_req2, VAL_NM_RQ):
    api_url = f"http://www.cbr.ru/scripts/XML_dynamic.asp"
    querystring = {'date_req1': date_req1, 'date_req2': date_req2, 'VAL_NM_RQ': VAL_NM_RQ, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_динамики_котировок_доллара_сша('02/03/2001', '14/03/2001', 'R01235')

import requests
                
def получение_динамики_сведений_об_остатках_средств_на_корреспондентских_счетах_кредитных_организаций(date_req1, date_req2):
    api_url = f"http://www.cbr.ru/scripts/XML_ostat.asp"
    querystring = {'date_req1': date_req1, 'date_req2': date_req2, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_динамики_сведений_об_остатках_средств_на_корреспондентских_счетах_кредитных_организаций('01/06/2001', '05/06/2001')

import requests
                
def получение_динамики_котировок_драгоценных_металлов(date_req1, date_req2):
    api_url = f"http://www.cbr.ru/scripts/xml_metall.asp"
    querystring = {'date_req1': date_req1, 'date_req2': date_req2, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_динамики_котировок_драгоценных_металлов('01/07/2001', '13/07/2001')

import requests
                
def получение_динамики_ставок_межбанковского_рынка(date_req1, date_req2):
    api_url = f"http://www.cbr.ru/scripts/xml_mkr.asp"
    querystring = {'date_req1': date_req1, 'date_req2': date_req2, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_динамики_ставок_межбанковского_рынка('01/07/2001', '13/07/2001')

import requests
                
def получение_динамики_ставок_привлечения_средств_по_депозитным_операциям_банка_россии_на_денежном_рынке(date_req1, date_req2):
    api_url = f"http://www.cbr.ru/scripts/xml_depo.asp"
    querystring = {'date_req1': date_req1, 'date_req2': date_req2, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_динамики_ставок_привлечения_средств_по_депозитным_операциям_банка_россии_на_денежном_рынке('01/07/2001', '13/07/2001')

import requests
                
def получение_новостей_сервера():
    api_url = f"http://www.cbr.ru/scripts/XML_News.asp"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_новостей_сервера()

import requests
                
def получение_соответствия_названий_кредитных_организаций_кодам_bic():
    api_url = f"http://www.cbr.ru/scripts/XML_bic.asp"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_соответствия_названий_кредитных_организаций_кодам_bic()

import requests
                
def получение_динамики_ставок__валютный_своп_(date_req1, date_req2):
    api_url = f"http://www.cbr.ru/scripts/xml_swap.asp"
    querystring = {'date_req1': date_req1, 'date_req2': date_req2, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_динамики_ставок__валютный_своп_('01/12/2002', '06/12/2002')

import requests
                
def получение_динамики_отпускных_цен_банка_россии_на_инвестиционные_монеты(date_req1, date_req2):
    api_url = f"http://www.cbr.ru/scripts/XMLCoinsBase.asp"
    querystring = {'date_req1': date_req1, 'date_req2': date_req2, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
получение_динамики_отпускных_цен_банка_россии_на_инвестиционные_монеты('01/12/2005', '06/12/2005')

import requests
                
def список_компаний_с_выявленными_признаками_нелегальной_деятельности_на_финансовом_рынке():
    api_url = f"http://www.cbr.ru/ref/blacklist/BlackList.xml"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
список_компаний_с_выявленными_признаками_нелегальной_деятельности_на_финансовом_рынке()

