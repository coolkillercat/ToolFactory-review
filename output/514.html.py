import requests
                
def get_word_definitions(word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    querystring = {'word': word, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_word_definitions('hello')

