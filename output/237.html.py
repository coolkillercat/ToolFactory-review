import requests
                
def get_all_ailments():
    api_url = f"https://mhw-db.com/ailments"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_ailments()

import requests
                
def get_a_specific_ailment(id):
    api_url = f"https://mhw-db.com/ailments/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_ailment(1)

import requests
                
def get_all_armor_pieces():
    api_url = f"https://mhw-db.com/armor"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_armor_pieces()

import requests
                
def get_a_specific_armor_piece(idOrSlug):
    api_url = f"https://mhw-db.com/armor/{idOrSlug}"
    querystring = {'idOrSlug': idOrSlug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_armor_piece(1 or 'leather-headgear')

import requests
                
def get_all_armor_sets():
    api_url = f"https://mhw-db.com/armor/sets"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_armor_sets()

import requests
                
def get_a_specific_armor_set(id):
    api_url = f"https://mhw-db.com/armor/sets/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_armor_set(20)

import requests
                
def get_all_charms():
    api_url = f"https://mhw-db.com/charms"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_charms()

import requests
                
def get_a_specific_charm(idOrSlug):
    api_url = f"https://mhw-db.com/charms/{idOrSlug}"
    querystring = {'idOrSlug': idOrSlug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_charm(234 or 'poison-charm')

import requests
                
def get_all_decorations():
    api_url = f"https://mhw-db.com/decorations"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_decorations()

import requests
                
def get_a_specific_decoration(idOrSlug):
    api_url = f"https://mhw-db.com/decorations/{idOrSlug}"
    querystring = {'idOrSlug': idOrSlug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_decoration(1 or 'antidote-jewel-1')

import requests
                
def get_all_events():
    api_url = f"https://mhw-db.com/events"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_events()

import requests
                
def get_a_specific_event(id):
    api_url = f"https://mhw-db.com/events/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_event(1)

import requests
                
def get_all_items():
    api_url = f"https://mhw-db.com/items"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_items()

import requests
                
def get_a_specific_item(id):
    api_url = f"https://mhw-db.com/items/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_item(1)

import requests
                
def get_all_locations():
    api_url = f"https://mhw-db.com/locations"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_locations()

import requests
                
def get_a_specific_location(id):
    api_url = f"https://mhw-db.com/locations/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_location(1)

import requests
                
def get_all_monsters():
    api_url = f"https://mhw-db.com/monsters"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_monsters()

import requests
                
def get_a_specific_monster(id):
    api_url = f"https://mhw-db.com/monsters/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_monster(1)

import requests
                
def get_all_motion_values():
    api_url = f"https://mhw-db.com/motion-values"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_motion_values()

import requests
                
def get_a_specific_motion_value(id):
    api_url = f"https://mhw-db.com/motion-values/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_motion_value(1)

import requests
                
def get_motion_values_by_weapon(weaponType):
    api_url = f"https://mhw-db.com/motion-values/{weaponType}"
    querystring = {'weaponType': weaponType, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_motion_values_by_weapon('great-sword')

import requests
                
def get_all_skills():
    api_url = f"https://mhw-db.com/skills"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_skills()

import requests
                
def get_a_specific_skill(idOrSlug):
    api_url = f"https://mhw-db.com/skills/{idOrSlug}"
    querystring = {'idOrSlug': idOrSlug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_skill(1 or 'poison-resistance')

import requests
                
def get_all_weapons():
    api_url = f"https://mhw-db.com/weapons"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_weapons()

import requests
                
def get_a_specific_weapon(idOrSlug):
    api_url = f"https://mhw-db.com/weapons/{idOrSlug}"
    querystring = {'idOrSlug': idOrSlug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_weapon(1 or 'buster-sword-1')

