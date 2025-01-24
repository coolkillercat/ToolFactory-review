import requests
                
def get_paragraphs(numberOfParagraphs):
    api_url = f"https://metaphorpsum.com/paragraphs/{numberOfParagraphs}"
    querystring = {'numberOfParagraphs': numberOfParagraphs, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_paragraphs(3)

import requests
                
def get_sentences(numberOfSentences):
    api_url = f"https://metaphorpsum.com/sentences/{numberOfSentences}"
    querystring = {'numberOfSentences': numberOfSentences, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sentences(5)

