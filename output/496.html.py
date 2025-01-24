import requests
                
def get_bible_verse_or_passage(BOOK, CHAPTER, VERSE):
    api_url = f"https://bible-api.com/BOOK+CHAPTER:VERSE"
    querystring = {'BOOK': BOOK, 'CHAPTER': CHAPTER, 'VERSE': VERSE, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_bible_verse_or_passage('john', 3, '16')

