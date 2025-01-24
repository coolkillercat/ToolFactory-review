import requests
                
def get_node_data(nid):
    api_url = f"https://www.drupal.org/api-d7/node/{nid}.json"
    querystring = {'nid': nid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_node_data(2773581)

import requests
                
def get_user_data(uid):
    api_url = f"https://www.drupal.org/api-d7/user/{uid}.json"
    querystring = {'uid': uid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_user_data(1)

import requests
                
def get_file_data(fid):
    api_url = f"https://www.drupal.org/api-d7/file/{fid}.json"
    querystring = {'fid': fid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_file_data(4688627)

import requests
                
def get_project_maintainers(project_id):
    api_url = f"https://www.drupal.org/project/{project_id}/maintainers.json"
    querystring = {'project_id': project_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_project_maintainers('drupal')

import requests
                
def get_drupalci_job_data(jobid):
    api_url = f"https://www.drupal.org/api-d7/pift_ci_job/{jobid}.json"
    querystring = {'jobid': jobid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_drupalci_job_data(57057)

import requests
                
def get_comments_for_a_node(node):
    api_url = f"https://www.drupal.org/api-d7/comment.json"
    querystring = {'node': node, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_comments_for_a_node(1978202)

import requests
                
def get_taxonomy_vocabulary_by_id(vid):
    api_url = f"https://www.drupal.org/api-d7/taxonomy_vocabulary.json"
    querystring = {'vid': vid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_taxonomy_vocabulary_by_id(7)

import requests
                
def get_taxonomy_terms_for_a_vocabulary(vocabulary):
    api_url = f"https://www.drupal.org/api-d7/taxonomy_term.json"
    querystring = {'vocabulary': vocabulary, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_taxonomy_terms_for_a_vocabulary(7)

import requests
                
def get_all_drupal_association_individual_members():
    api_url = f"https://www.drupal.org/api-d7/user.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_drupal_association_individual_members()

import requests
                
def get_all_drupal_association_organization_members():
    api_url = f"https://www.drupal.org/api-d7/node.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_drupal_association_organization_members()

