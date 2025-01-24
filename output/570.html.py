import requests
                
def player_profile(username):
    api_url = f"https://api.chess.com/pub/player/{username}"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
player_profile('erik')

import requests
                
def titled_players(title_abbrev):
    api_url = f"https://api.chess.com/pub/titled/{title-abbrev}"
    querystring = {'title_abbrev': title_abbrev, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
titled_players('GM')

import requests
                
def player_stats(username):
    api_url = f"https://api.chess.com/pub/player/{username}/stats"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
player_stats('erik')

import requests
                
def player_online_status(username):
    api_url = f"https://api.chess.com/pub/player/{username}/is-online"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
player_online_status('erik')

import requests
                
def current_daily_chess(username):
    api_url = f"https://api.chess.com/pub/player/{username}/games"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
current_daily_chess('erik')

import requests
                
def to_move_daily_chess(username):
    api_url = f"https://api.chess.com/pub/player/{username}/games/to-move"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
to_move_daily_chess('erik')

import requests
                
def list_of_monthly_archives(username):
    api_url = f"https://api.chess.com/pub/player/{username}/games/archives"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_of_monthly_archives('erik')

import requests
                
def complete_monthly_archives(username, YYYY, MM):
    api_url = f"https://api.chess.com/pub/player/{username}/games/{YYYY}/{MM}"
    querystring = {'username': username, 'YYYY': YYYY, 'MM': MM, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
complete_monthly_archives('erik', '2022', '10')

import requests
                
def multi_game_pgn_download(username, YYYY, MM):
    api_url = f"https://api.chess.com/pub/player/{username}/games/{YYYY}/{MM}/pgn"
    querystring = {'username': username, 'YYYY': YYYY, 'MM': MM, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
multi_game_pgn_download('erik', '2022', '10')

import requests
                
def player_s_clubs(username):
    api_url = f"https://api.chess.com/pub/player/{username}/clubs"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
player_s_clubs('erik')

import requests
                
def player_matches(username):
    api_url = f"https://api.chess.com/pub/player/{username}/matches"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
player_matches('erik')

import requests
                
def player_s_tournaments(username):
    api_url = f"https://api.chess.com/pub/player/{username}/tournaments"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
player_s_tournaments('erik')

import requests
                
def club_profile(url_ID):
    api_url = f"https://api.chess.com/pub/club/{url-ID}"
    querystring = {'url_ID': url_ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
club_profile('chess-com-developer-community')

import requests
                
def club_members(url_ID):
    api_url = f"https://api.chess.com/pub/club/{url-ID}/members"
    querystring = {'url_ID': url_ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
club_members('chess-com-developer-community')

import requests
                
def club_matches(ID):
    api_url = f"https://api.chess.com/pub/club/{ID}/matches"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
club_matches('team-usa-southwest')

import requests
                
def tournament(url_ID):
    api_url = f"https://api.chess.com/pub/tournament/{url-ID}"
    querystring = {'url_ID': url_ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
tournament('-33rd-chesscom-quick-knockouts-1401-1600')

import requests
                
def tournament_s_round(url_ID, round):
    api_url = f"https://api.chess.com/pub/tournament/{url-ID}/{round}"
    querystring = {'url_ID': url_ID, 'round': round, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
tournament_s_round('-33rd-chesscom-quick-knockouts-1401-1600', '1')

import requests
                
def tournament_s_round_group(url_ID, round, group):
    api_url = f"https://api.chess.com/pub/tournament/{url-ID}/{round}/{group}"
    querystring = {'url_ID': url_ID, 'round': round, 'group': group, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
tournament_s_round_group('-33rd-chesscom-quick-knockouts-1401-1600', '1', '1')

import requests
                
def daily_team_match(ID):
    api_url = f"https://api.chess.com/pub/match/{ID}"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
daily_team_match('12803')

import requests
                
def daily_team_match_board(ID, board):
    api_url = f"https://api.chess.com/pub/match/{ID}/{board}"
    querystring = {'ID': ID, 'board': board, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
daily_team_match_board('12803', '1')

import requests
                
def live_team_match(ID):
    api_url = f"https://api.chess.com/pub/match/live/{ID}"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
live_team_match('5833')

import requests
                
def live_team_match_board(ID, board):
    api_url = f"https://api.chess.com/pub/match/live/{ID}/{board}"
    querystring = {'ID': ID, 'board': board, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
live_team_match_board('5833', '1')

import requests
                
def country_profile(iso):
    api_url = f"https://api.chess.com/pub/country/{iso}"
    querystring = {'iso': iso, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
country_profile('IT')

import requests
                
def country_players(iso):
    api_url = f"https://api.chess.com/pub/country/{iso}/players"
    querystring = {'iso': iso, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
country_players('IT')

import requests
                
def country_clubs(iso):
    api_url = f"https://api.chess.com/pub/country/{iso}/clubs"
    querystring = {'iso': iso, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
country_clubs('IT')

import requests
                
def daily_puzzle():
    api_url = f"https://api.chess.com/pub/puzzle"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
daily_puzzle()

import requests
                
def random_daily_puzzle():
    api_url = f"https://api.chess.com/pub/puzzle/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
random_daily_puzzle()

import requests
                
def streamers():
    api_url = f"https://api.chess.com/pub/streamers"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
streamers()

import requests
                
def leaderboards():
    api_url = f"https://api.chess.com/pub/leaderboards"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
leaderboards()

