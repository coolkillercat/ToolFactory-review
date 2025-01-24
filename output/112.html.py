import requests
                
def create_diagram__get_(diagram_type, output_format, encoded_diagram):
    api_url = f"https://kroki.io/{diagram_type}/{output_format}/{encoded_diagram}"
    querystring = {'diagram_type': diagram_type, 'output_format': output_format, 'encoded_diagram': encoded_diagram, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_diagram__get_('graphviz', 'svg', 'eNpLyUwvSizIUHBXqPZIzcnJ17ULzy_KSanlAgB1EAjQ')

import requests
                
def create_diagram__post_(diagram_type, output_format, diagram_source):
    api_url = f"https://kroki.io/{diagram_type}/{output_format}"
    payload = {'diagram_type': diagram_type, 'output_format': output_format, 'diagram_source': diagram_source, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_diagram__post_('graphviz', 'svg', 'digraph G {Hello->World}')

