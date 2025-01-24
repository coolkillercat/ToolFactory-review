import requests
                
def get_all_teams():
    api_url = f"https://api.balldontlie.io/v1/teams"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_teams()

import requests
                
def get_a_specific_team(ID):
    api_url = f"https://api.balldontlie.io/v1/teams/{ID}"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_team(1)

import requests
                
def get_all_players():
    api_url = f"https://api.balldontlie.io/v1/players"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_players()

import requests
                
def get_a_specific_player(ID):
    api_url = f"https://api.balldontlie.io/v1/players/{ID}"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_player(19)

import requests
                
def get_all_games():
    api_url = f"https://api.balldontlie.io/v1/games"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_games()

import requests
                
def get_a_specific_game(ID):
    api_url = f"https://api.balldontlie.io/v1/games/{ID}"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_specific_game(1)

import requests
                
def get_all_stats():
    api_url = f"https://api.balldontlie.io/v1/stats"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_stats()

import requests
                
def get_averages(season, player_ids):
    api_url = f"https://api.balldontlie.io/v1/season_averages"
    querystring = {'season': season, 'player_ids': player_ids, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_averages(2023, [1, 2])

import requests
                
def get_all_advanced_stats():
    api_url = f"https://api.balldontlie.io/v1/stats/advanced"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_advanced_stats()

import requests
                
def get_live_box_scores():
    api_url = f"https://api.balldontlie.io/v1/box_scores/live"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_live_box_scores()

import requests
                
def get_box_scores(date):
    api_url = f"https://api.balldontlie.io/v1/box_scores"
    querystring = {'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_box_scores('2024-02-07')

import requests
                
def get_all_active_players():
    api_url = f"https://api.balldontlie.io/v1/players/active"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_active_players()

import requests
                
def get_team_standings(season):
    api_url = f"https://api.balldontlie.io/v1/standings"
    querystring = {'season': season, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_team_standings(2023)

import requests
                
def get_leaders(stat_type, season):
    api_url = f"https://api.balldontlie.io/v1/leaders"
    querystring = {'stat_type': stat_type, 'season': season, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_leaders('pts', 2023)

import requests
                
def get_betting_odds(date, game_id):
    api_url = f"https://api.balldontlie.io/v1/odds"
    querystring = {'date': date, 'game_id': game_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_betting_odds('2024-04-01', 1)

