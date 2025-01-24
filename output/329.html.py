import requests
                
def list_editions():
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_editions()

import requests
                
def list_editions__minified_():
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions.min.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_editions__minified_()

import requests
                
def get_edition(editionName):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}.json"
    querystring = {'editionName': editionName, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_edition('ben-muhiuddinkhan')

import requests
                
def get_edition__latin_script_(editionName):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}-la.json"
    querystring = {'editionName': editionName, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_edition__latin_script_('ben-muhiuddinkhan')

import requests
                
def get_edition__latin_script_with_diacritical_marks_(editionName):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}-lad.json"
    querystring = {'editionName': editionName, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_edition__latin_script_with_diacritical_marks_('ben-muhiuddinkhan')

import requests
                
def get_chapter(editionName, ChapterNo):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}/{ChapterNo}.json"
    querystring = {'editionName': editionName, 'ChapterNo': ChapterNo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_chapter('ben-muhiuddinkhan', 5)

import requests
                
def get_chapter__minified_(editionName, ChapterNo):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}/{ChapterNo}.min.json"
    querystring = {'editionName': editionName, 'ChapterNo': ChapterNo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_chapter__minified_('ben-muhiuddinkhan', 5)

import requests
                
def get_verse(editionName, ChapterNo, VerseNo):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}/{ChapterNo}/{VerseNo}.json"
    querystring = {'editionName': editionName, 'ChapterNo': ChapterNo, 'VerseNo': VerseNo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_verse('ben-muhiuddinkhan', 5, 10)

import requests
                
def get_juz(editionName, juzNo):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}/juzs/{juzNo}.json"
    querystring = {'editionName': editionName, 'juzNo': juzNo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_juz('ben-muhiuddinkhan', 3)

import requests
                
def get_ruku(editionName, rukuNo):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}/rukus/{rukuNo}.json"
    querystring = {'editionName': editionName, 'rukuNo': rukuNo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_ruku('ben-muhiuddinkhan', 1)

import requests
                
def get_page(editionName, pageNo):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}/pages/{pageNo}.json"
    querystring = {'editionName': editionName, 'pageNo': pageNo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_page('ben-muhiuddinkhan', 1)

import requests
                
def get_manzil(editionName, manzilNo):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}/manzils/{manzilNo}.json"
    querystring = {'editionName': editionName, 'manzilNo': manzilNo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_manzil('ben-muhiuddinkhan', 1)

import requests
                
def get_maqra(editionName, maqraNo):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editionName}/maqras/{maqraNo}.json"
    querystring = {'editionName': editionName, 'maqraNo': maqraNo, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_maqra('ben-muhiuddinkhan', 1)

import requests
                
def get_quran_info():
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_quran_info()

import requests
                
def list_fonts():
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/fonts.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_fonts()

