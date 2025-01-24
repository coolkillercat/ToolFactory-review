import requests
                
def job_title_autocomplete(begins_with):
    api_url = f"http://api.dataatwork.org/v1/jobs/autocomplete"
    querystring = {'begins_with': begins_with, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
job_title_autocomplete('software')

import requests
                
def normalize_job_title(job_title):
    api_url = f"http://api.dataatwork.org/v1/jobs/normalize"
    querystring = {'job_title': job_title, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
normalize_job_title('ninja')

import requests
                
def get_job_titles_from_o_net_code(onet_soc_code):
    api_url = f"http://api.dataatwork.org/v1/jobs/{onet_soc_code}"
    querystring = {'onet_soc_code': onet_soc_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_job_titles_from_o_net_code('41-3031.00')

import requests
                
def skill_name_autocomplete(begins_with):
    api_url = f"http://api.dataatwork.org/v1/skills/autocomplete"
    querystring = {'begins_with': begins_with, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
skill_name_autocomplete('java')

import requests
                
def normalize_skill_name(skill_name):
    api_url = f"http://api.dataatwork.org/v1/skills/normalize"
    querystring = {'skill_name': skill_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
normalize_skill_name('java')

import requests
                
def get_normalized_skill_uuid_from_skill_onet_id(onet_soc_code):
    api_url = f"http://api.dataatwork.org/v1/skills/{onet_soc_code}"
    querystring = {'onet_soc_code': onet_soc_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_normalized_skill_uuid_from_skill_onet_id('13-2011.01')

import requests
                
def get_associated_skills_for_a_job(uuid):
    api_url = f"http://api.dataatwork.org/v1/jobs/{uuid}/related_skills"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_associated_skills_for_a_job('2995ce54b9dd5944b0528b734cfc5b6d')

import requests
                
def get_associated_jobs_for_a_job(uuid):
    api_url = f"http://api.dataatwork.org/v1/jobs/{uuid}/related_jobs"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_associated_jobs_for_a_job('2995ce54b9dd5944b0528b734cfc5b6d')

import requests
                
def get_associated_jobs_for_a_skill(uuid):
    api_url = f"http://api.dataatwork.org/v1/skills/{uuid}/related_jobs"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_associated_jobs_for_a_skill('2c77c703bd66e104c78b1392c3203362')

import requests
                
def get_associated_skills_for_a_skill(uuid):
    api_url = f"http://api.dataatwork.org/v1/skills/{uuid}/related_skills"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_associated_skills_for_a_skill('4d70921065c00a293597936b693345aa')

import requests
                
def get_skills_name_and_frequency_for_a_skill_uuid(uuid):
    api_url = f"http://api.dataatwork.org/v1/skills/{uuid}"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_skills_name_and_frequency_for_a_skill_uuid('4d70921065c00a293597936b693345aa')

import requests
                
def get_job_name_for_a_job_uuid(uuid):
    api_url = f"http://api.dataatwork.org/v1/jobs/{uuid}"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_job_name_for_a_job_uuid('5d12ef84fe6bc1ead14db1b113188625')

import requests
                
def retrieve_all_jobs():
    api_url = f"http://api.dataatwork.org/v1/jobs"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_all_jobs()

import requests
                
def retrieve_all_skills():
    api_url = f"http://api.dataatwork.org/v1/skills"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_all_skills()

