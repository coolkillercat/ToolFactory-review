import requests
                
def retrieve_all_stations():
    api_url = f"https://api.irail.be/stations/{?format,lang}"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_all_stations()

import requests
                
def retrieve_a_liveboard(station):
    api_url = f"https://api.irail.be/liveboard/{?id,station,date,time,arrdep,lang,format,alerts}"
    querystring = {'station': station, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_a_liveboard('Gent-Sint-Pieters')

import requests
                
def retrieve_connections(from, to):
    api_url = f"https://api.irail.be/connections/{?from,to,date,time,timesel,format,lang,typeOfTransport,alerts,results}"
    querystring = {'from': from, 'to': to, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_connections('Gent-Sint-Pieters', 'Mechelen')

import requests
                
def retrieve_a_vehicle(id):
    api_url = f"https://api.irail.be/vehicle/{?id,date,format,lang,alerts}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_a_vehicle('BE.NMBS.IC1832')

import requests
                
def retrieve_the_composition_for_a_train(id):
    api_url = f"https://api.irail.be/composition/{?format,id,data,lang}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_the_composition_for_a_train('S51507')

import requests
                
def retrieve_the_current_disturbances():
    api_url = f"https://api.irail.be/disturbances/{?format,lineBreakCharacter,lang}"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_the_current_disturbances()

import requests
                
def post_feedback_to_irail(connection, from, date, vehicle, occupancy):
    api_url = f"https://api.irail.be/feedback/occupancy"
    payload = {'connection': connection, 'from': from, 'date': date, 'vehicle': vehicle, 'occupancy': occupancy, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
post_feedback_to_irail('http://irail.be/connections/8871308/20160722/IC4516', 'http://irail.be/stations/NMBS/008871308', '20160722', 'http://irail.be/vehicle/IC4516', 'http://api.irail.be/terms/low')

import requests
                
def retrieve_the_last_logs():
    api_url = f"https://api.irail.be/logs/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_the_last_logs()

