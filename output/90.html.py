import requests
                
def get_edition():
    api_url = f"http://api.alquran.cloud/v1/edition"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_edition()

import requests
                
def get_edition_by_language(language):
    api_url = f"http://api.alquran.cloud/v1/edition/language/{{language}}"
    querystring = {'language': language, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_edition_by_language('en')

import requests
                
def get_edition_by_type(type):
    api_url = f"http://api.alquran.cloud/v1/edition/type/{{type}}"
    querystring = {'type': type, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_edition_by_type('translation')

import requests
                
def get_edition_by_format(format):
    api_url = f"http://api.alquran.cloud/v1/edition/format/{{format}}"
    querystring = {'format': format, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_edition_by_format('text')

import requests
                
def get_complete_quran_edition(edition):
    api_url = f"http://api.alquran.cloud/v1/quran/{{edition}}"
    querystring = {'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_complete_quran_edition('en.asad')

import requests
                
def get_juz(juz, edition):
    api_url = f"http://api.alquran.cloud/v1/juz/{{juz}}/{{edition}}"
    querystring = {'juz': juz, 'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_juz(30, 'en.asad')

import requests
                
def get_surah(surah, edition):
    api_url = f"http://api.alquran.cloud/v1/surah/{{surah}}/{{edition}}"
    querystring = {'surah': surah, 'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_surah(114, 'en.asad')

import requests
                
def get_ayah(reference, edition):
    api_url = f"http://api.alquran.cloud/v1/ayah/{{reference}}/{{edition}}"
    querystring = {'reference': reference, 'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_ayah('2:255', 'en.asad')

import requests
                
def search(keyword, surah, edition_or_language):
    api_url = f"http://api.alquran.cloud/v1/search/{{keyword}}/{{surah}}/{{edition or language}}"
    querystring = {'keyword': keyword, 'surah': 'all', 'edition_or_language': 'en', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search('Abraham', '37', 'en.pickthall')

import requests
                
def get_manzil(manzil, edition):
    api_url = f"http://api.alquran.cloud/v1/manzil/{{manzil}}/{{edition}}"
    querystring = {'manzil': manzil, 'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_manzil(7, 'en.asad')

import requests
                
def get_ruku(ruku, edition):
    api_url = f"http://api.alquran.cloud/v1/ruku/{{ruku}}/{{edition}}"
    querystring = {'ruku': ruku, 'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_ruku(7, 'en.asad')

import requests
                
def get_page(page, edition):
    api_url = f"http://api.alquran.cloud/v1/page/{{page}}/{{edition}}"
    querystring = {'page': page, 'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_page(1, 'en.asad')

import requests
                
def get_hizb_quarter(hizb, edition):
    api_url = f"http://api.alquran.cloud/v1/hizbQuarter/{{hizb}}/{{edition}}"
    querystring = {'hizb': hizb, 'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_hizb_quarter(1, 'en.asad')

import requests
                
def get_sajda(edition):
    api_url = f"http://api.alquran.cloud/v1/sajda/{{edition}}"
    querystring = {'edition': 'quran-uthmani', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sajda('en.asad')

import requests
                
def get_meta():
    api_url = f"http://api.alquran.cloud/v1/meta"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_meta()

