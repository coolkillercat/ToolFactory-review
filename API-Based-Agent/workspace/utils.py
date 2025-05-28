import importlib.util
import json
import os
import re
import sys
from os import path

import requests


def replace_substrings(match):
    return '1234567'


# input yaml formatted api, get md file for that api
def get_md_by_api(api):
    yaml_api_sub = re.sub(r'\{[^}]+\}', '1234567', api)
    method = yaml_api_sub.split(' ')[0]
    if '/api/v4/' not in yaml_api_sub:
        return None
    yaml_api = (yaml_api_sub.split(' ')[1]).split('/api/v4/')[1]
    entries = os.listdir('gitlab_api')
    for entry in entries:
        md_file = os.path.join('gitlab_api', entry)
        if not (os.path.isfile(md_file) and md_file.endswith('.md')):
            continue
        with open(md_file, 'r') as file:
            data = file.read()
        test = re.sub(r':\w+', replace_substrings, data)
        if (
            f'{method.upper()} {yaml_api}\n' in test
            or f'{method.upper()} /{yaml_api}\n' in test
        ):
            if f'{method.upper()} {yaml_api}\n' in test:
                mdapi_sub = f'{method.upper()} {yaml_api}\n'
            if f'{method.upper()} /{yaml_api}\n' in test:
                mdapi_sub = f'{method.upper()} /{yaml_api}\n'
            index = test.find(mdapi_sub)
            start = data.rfind('## ', 0, index)
            end = data.find('## ', start + 3)
            if end == -1:
                return (data[start:]).strip()
            else:
                return (data[start:end]).strip()
    return f'No such API found: {api}.'


def get_api_documentation_gitlab(api: str) -> str:
    """
    Returns the markdown documentation of the given API.
    Args: api: str: The API whose documentations to retrieve. For example, 'get /api/v4/projects/{id}/repository/commits'.
    """
    return get_md_by_api(api)


def get_shopping_readme():
    with open('shopping_readme/performing-searches.md', 'r') as f:
        searchCriteriaDoc = f.read()
    with open('shopping_readme/retrieve-filtered-responses.md', 'r') as f:
        retrieveFilteredDoc = f.read()
    with open('shopping_readme/search-endpoint.md', 'r') as f:
        searchDoc = f.read()
    with open('shopping_readme/order-create-quote.md', 'r') as f:
        quoteDoc = f.read()
    with open('shopping_readme/order-add-items.md', 'r') as f:
        itemDoc = f.read()
    with open('shopping_readme/order-shipping-cost.md', 'r') as f:
        shipCostDoc = f.read()
    with open('shopping_readme/order-shipping-billing.md', 'r') as f:
        shipBillDoc = f.read()
    with open('shopping_readme/order-create-order.md', 'r') as f:
        orderDoc = f.read()
    return (
        searchCriteriaDoc,
        retrieveFilteredDoc,
        searchDoc,
        quoteDoc,
        itemDoc,
        shipCostDoc,
        shipBillDoc,
        orderDoc,
    )


def get_shopping_html_api_doc(html_page):
    shopping_html_api_doc = {
        'description': f'Retrieve the content in the HTML page {html_page}',
        'responses': {
            '200': {
                'description': '200 Success.',
                'content': {
                    'text/plain:': {
                        'schema': {
                            'type': 'string',
                            'example': "<!doctype html>\n<html lang='en'>\n ..... SOME HTML CONTENT ..... </html>\n",
                        }
                    }
                },
            },
            'default': {
                'description': 'Unexpected error',
                'content': {
                    'text/plain:': {
                        'schema': {'$ref': '#/components/schemas/error-response'}
                    }
                },
            },
        },
    }
    return shopping_html_api_doc


def list_tools(site='shopping'):
    """
    Lists available tools for a specific site by reading the tool_descriptions.json file.

    Args:
        site (str): The site to list tools for (default: 'shopping')

    Returns:
        str: A formatted string listing all available tools and their descriptions

    Example:
        >>> list_tools()
        Available tools:
        - search_customers_GET: Searches for customers based on criteria
        - create_customer_POST: Creates a new customer
        ...
    """
    import json
    import os
    from os import path

    print(f"DEBUG: Starting list_tools for site '{site}'", file=sys.stderr)

    try:
        # Look for the tool_descriptions.json file in both potential locations
        descriptions_paths = [
            path.join(path.dirname(path.abspath(__file__)), 'api', site, 'tool_descriptions.json'),
            path.join(path.dirname(path.abspath(__file__)), 'workspace', 'api', site, 'tool_descriptions.json')
        ]
        
        for descriptions_path in descriptions_paths:
            print(
                f'DEBUG: Looking for tool descriptions at: {descriptions_path}',
                file=sys.stderr,
            )
            print(f'DEBUG: File exists: {path.exists(descriptions_path)}', file=sys.stderr)

            if path.exists(descriptions_path):
                # Read and parse the JSON file
                with open(descriptions_path, 'r') as f:
                    tools = json.load(f)
                    print(
                        'DEBUG: Successfully read tool_descriptions.json', file=sys.stderr
                    )

                    # Format the tools into a readable string
                    result = 'Available tools:\n'
                    for tool_name, description in tools.items():
                        result += f'- {tool_name}: {description}\n'
                    return result.strip()
        
        # If we get here, try both potential tool directories
        tools_dirs = [
            path.join(path.dirname(path.abspath(__file__)), 'api', site, 'tools'),
            path.join(path.dirname(path.abspath(__file__)), 'workspace', 'api', site, 'tools')
        ]
        
        for tools_dir in tools_dirs:
            print(
                f'DEBUG: Checking tools directory: {tools_dir}',
                file=sys.stderr,
            )

            if path.exists(tools_dir):
                try:
                    tool_files = [
                        f
                        for f in os.listdir(tools_dir)
                        if f.endswith('.py') and not f.startswith('__')
                    ]
                    print(
                        f'DEBUG: Found {len(tool_files)} tool files: {tool_files}',
                        file=sys.stderr,
                    )
                    tool_names = [f[:-3] for f in tool_files]  # Remove .py extension
                    return 'Available tools:\n' + '\n'.join(
                        f'- {name}' for name in tool_names
                    )
                except Exception as e:
                    print(f'ERROR scanning tools directory: {str(e)}', file=sys.stderr)
                    continue
        
        return f"No tools directory or descriptions file found for site '{site}'"
    except Exception as e:
        print(f'CRITICAL ERROR in list_tools: {str(e)}', file=sys.stderr)
        return f'Critical error in list_tools: {str(e)}'


def get_documentation(tool_name, site='shopping'):
    """
    Returns documentation for a specific tool.
    First tries to retrieve the docstring from the function directly.
    If no docstring is available, falls back to the site's documentation file.
    Also extracts an example usage from the `if __name__ == '__main__':` section if available.

    Args:
        tool_name (str): The name of the tool (e.g., 'search_customers_GET')
        site (str): The site to get documentation for (default: 'shopping')

    Returns:
        str: Documentation for the tool including description, parameters, and example
    """
    # Import necessary modules
    import re
    import sys

    # Try both potential module paths
    module_paths = [
        path.join(path.dirname(path.abspath(__file__)), 'api', site, 'tools', f'{tool_name}.py'),
        path.join(path.dirname(path.abspath(__file__)), 'workspace', 'api', site, 'tools', f'{tool_name}.py')
    ]
    
    module_path = None
    for potential_path in module_paths:
        print(f'DEBUG: Looking for module at {potential_path}', file=sys.stderr)
        if path.exists(potential_path):
            module_path = potential_path
            break
    
    if not module_path:
        return f"No module found for tool '{tool_name}' in site '{site}'"

    # Extract example from the file if it exists
    example_usage = None
    try:
        with open(module_path, 'r') as f:
            file_content = f.read()

        # Find the main section and extract the first line after it
        main_pattern = r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:"
        main_match = re.search(main_pattern, file_content)

        if main_match:
            # Find the first non-empty, non-comment line after the main block
            after_main = file_content[main_match.end() :]
            lines = after_main.split('\n')

            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    # This is likely a function call - extract it
                    if '=' in line:
                        example_usage = line.split('=', 1)[1].strip()
                    else:
                        example_usage = line.strip()
                    break
    except Exception as e:
        print(f'Error extracting example: {str(e)}', file=sys.stderr)

    # Try to get the function's docstring first
    try:
        # Find the base name (remove _GET, _POST, etc.)
        base_name = None
        for suffix in ['_GET', '_POST', '_PUT', '_DELETE']:
            if tool_name.endswith(suffix):
                base_name = tool_name[: -len(suffix)]
                break
        if not base_name:
            base_name = tool_name

        # Import the module dynamically
        spec = importlib.util.spec_from_file_location(tool_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # First try to find a function with the same name as the file (without _GET/_POST suffix)
        target_function = getattr(module, base_name, None)

        # If not found, get the first function defined in the module that's not a built-in
        if target_function is None:
            functions = [
                f
                for f in dir(module)
                if callable(getattr(module, f)) and not f.startswith('_')
            ]
            if functions:
                target_function = getattr(module, functions[0])

        # If we have the function and its docstring
        if target_function and target_function.__doc__:
            # Return just the docstring and example in the required format
            docstring = target_function.__doc__.strip()

            # Add example if found
            if example_usage:
                result = f'"""\n{docstring}\n""" example: {example_usage}'
            else:
                result = f'"""\n{docstring}\n"""'

            return result
    except Exception as e:
        # If there's an error getting the docstring, log it and continue to fallback method
        print(f'Error getting docstring for {tool_name}: {str(e)}', file=sys.stderr)

    # If we reached here, no valid docstring was found - fallback to existing documentation from txt file
    # Extract method from tool name
    method = None
    if '_GET' in tool_name:
        method = 'GET'
        base_name = tool_name.replace('_GET', '')
    elif '_POST' in tool_name:
        method = 'POST'
        base_name = tool_name.replace('_POST', '')
    elif '_PUT' in tool_name:
        method = 'PUT'
        base_name = tool_name.replace('_PUT', '')
    elif '_DELETE' in tool_name:
        method = 'DELETE'
        base_name = tool_name.replace('_DELETE', '')
    else:
        base_name = tool_name

    # Load the documentation file based on site
    doc_filename = f'{site}.txt'
    doc_paths = [
        path.join(path.dirname(path.abspath(__file__)), 'api', site, doc_filename),
        path.join(path.dirname(path.abspath(__file__)), 'workspace', 'api', site, doc_filename)
    ]
    
    doc_path = None
    for potential_path in doc_paths:
        if path.exists(potential_path):
            doc_path = potential_path
            break
            
    if not doc_path:
        return f"No documentation found for tool '{tool_name}' in site '{site}'"

    try:
        with open(doc_path, 'r') as f:
            doc_data = json.load(f)
            endpoints = doc_data.get('endpoints', [])

            # Try different approaches to find matching endpoint
            # Approach 1: Try to find by name first
            for ep in endpoints:
                ep_name = ep.get('name', '')
                if ep_name and base_name.lower() in ep_name.lower().replace(' ', '_'):
                    if method is None or ep.get('method', '') == method:
                        # Found a match in txt file
                        description = ep.get('description', '')

                        # Build parameters section from required and optional parameters
                        param_text = []
                        for param in ep.get('required_parameters', []):
                            param_name = param.get('name', '')
                            param_desc = param.get('description', '')
                            param_text.append(f'- {param_name}: {param_desc}')

                        for param in ep.get('optional_parameters', []):
                            param_name = param.get('name', '')
                            param_desc = param.get('description', '')
                            param_text.append(f'- {param_name}: {param_desc}')

                        # Combine into docstring format
                        docstring = f'{description}\n\nParameters:\n' + '\n'.join(
                            param_text
                        )

                        # Add example if found
                        if example_usage:
                            result = f'"""\n{docstring}\n""" example: {example_usage}'
                        else:
                            result = f'"""\n{docstring}\n"""'

                        return result

            # If we failed to find a match with any approach
            result = f"No documentation found for tool '{tool_name}' in site '{site}'"
            if example_usage:
                result = f'{result} example: {example_usage}'
            return result

    except json.JSONDecodeError:
        result = f"Error: Documentation file for site '{site}' is not valid JSON"
        if example_usage:
            result = f'{result} example: {example_usage}'
        return result


def call_function(tool_name, site='shopping', **kwargs):
    """
    Dynamically imports and calls a tool function.

    Args:
        tool_name (str): The name of the tool function to call (e.g., 'search_customers_GET')
        site (str): The site to call the tool for (default: 'shopping')
        **kwargs: Keyword arguments to pass to the function, matching the parameters from documentation

    Returns:
        The result of the function call, typically a dict with API response

    Example:
        >>> call_function('search_customers_GET',
                search_field='email',
                search_value='user@example.com',
                condition_type='eq')
        {
            'status_code': 200,
            'content': {
                'items': [...],
                'total_count': 1
            }
        }
    """
    import json
    import re
    import sys

    # Try both potential module paths
    module_paths = [
        path.join(path.dirname(path.abspath(__file__)), 'api', site, 'tools', f'{tool_name}.py'),
        path.join(path.dirname(path.abspath(__file__)), 'workspace', 'api', site, 'tools', f'{tool_name}.py')
    ]
    
    module_path = None
    for potential_path in module_paths:
        if path.exists(potential_path):
            module_path = potential_path
            break
            
    if not module_path:
        return f"Error: Module not found for tool '{tool_name}' in site '{site}'"
        
    api_url_value = None

    try:
        base_name = None
        for suffix in ['_GET', '_POST', '_PUT', '_DELETE']:
            if tool_name.endswith(suffix):
                base_name = tool_name[: -len(suffix)]
                break
        if not base_name:
            base_name = tool_name

        spec = importlib.util.spec_from_file_location(tool_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        target_function = getattr(module, base_name, None)
        if target_function is None:
            functions = [
                f
                for f in dir(module)
                if callable(getattr(module, f)) and not f.startswith('_')
            ]
            if functions:
                target_function = getattr(module, functions[0])

        # Extract the api_url for logging (not token URLs)
        with open(module_path, 'r') as f:
            file_content = f.read()
            # Only match api_url assignments that are not for token endpoints
            api_url_matches = re.findall(
                r"api_url\s*=\s*[\"']([^\"']+)[\"']", file_content
            )
            # Filter out any api_url that looks like a token endpoint
            api_url_matches = [
                u for u in api_url_matches if 'token' not in u.lower()
            ]
            if api_url_matches:
                api_url_value = api_url_matches[0]

        # Print the tool name, site, and parameters before the call
        print(f'tool: {tool_name}')
        print(f'site: {site}')
        print(f"parameter: {', '.join([f'{k}={v}' for k, v in kwargs.items()])}")
        if api_url_value:
            print(f'api_url: {api_url_value}')
        sys.stdout.flush()

        if target_function:
            result = target_function(**kwargs)

            # Always print the real API call URL after the call
            url_printed = False
            try:
                if isinstance(result, requests.Response):
                    # Only print if not a token endpoint
                    if 'token' not in result.url.lower():
                        print(f'url: {result.url}')
                        url_printed = True
                        print(f'status_code: {result.status_code}')
                        try:
                            print(f'content: {result.json()}')
                        except Exception:
                            print(f'content: {result.text}')
                    sys.stdout.flush()
            except Exception:
                pass
            # If not a Response, but we have api_url_value, print it as the url
            if not url_printed and api_url_value:
                print(f'url: {api_url_value}')
                sys.stdout.flush()
            # If the result is a dict and contains a 'url' key, print it
            if (
                not url_printed
                and isinstance(result, dict)
                and 'url' in result
                and 'token' not in str(result['url']).lower()
            ):
                print(f"url: {result['url']}")
                sys.stdout.flush()
            # Always print the parameters and flush
            print(
                f"parameter: {', '.join([f'{k}={v}' for k, v in kwargs.items()])}"
            )
            sys.stdout.flush()
            # If the result is a dict, print as JSON
            if isinstance(result, dict):
                print(f'content: {json.dumps(result)}')
            return result
        else:
            return f"Error: Could not find target function in module '{tool_name}'"
    except Exception as e:
        import traceback

        traceback_str = traceback.format_exc()
        return f"Error calling function '{tool_name}': {str(e)}\n{traceback_str}"


def call_direct(method, url, headers=None, body=None, site='shopping'):
    """
    Makes a direct API call for methods not supported by tool functions (PUT/DELETE).

    Args:
        method (str): HTTP method ('PUT', 'DELETE')
        url (str): Full URL for the API call
        headers (dict): Headers to include in the request
        body (dict): JSON body for the request
        site (str): The site to use for token retrieval (default: 'shopping')

    Returns:
        dict: Response information including status code and content

    Example:
        >>> call_direct(
        ...     method='PUT',
        ...     url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/customers/1',
        ...     headers={'Authorization': 'Bearer token'},
        ...     body={'customer': {'email': 'new@example.com'}}
        ... )
        {
            'status_code': 200,
            'content': {'id': 1, 'email': 'new@example.com', ...}
        }
    """
    if headers is None:
        headers = {}

    # Add authorization if not provided - for shopping site
    if 'Authorization' not in headers and site == 'shopping':
        from utils import get_shopping_customer_auth_token

        headers['Authorization'] = f'Bearer {get_shopping_customer_auth_token()}'

    # Add content type if not provided
    if 'Content-Type' not in headers and body is not None:
        headers['Content-Type'] = 'application/json'

    try:
        if method == 'PUT':
            response = requests.put(url, json=body, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, json=body, headers=headers)
        else:
            return f"Method '{method}' not supported by call_direct. Use call_function for GET/POST."

        # Return response information
        try:
            return {'status_code': response.status_code, 'content': response.json()}
        except:
            return {'status_code': response.status_code, 'content': response.text}
    except Exception as e:
        return f'Error making API call: {str(e)}'


def get_api_documentation_map(api: str) -> str:
    file = 'map.txt'
    with open(file, 'r') as f:
        f = f.readlines()
    f = [line for line in f if line.strip() != '']
    title = ''
    output = ''
    output += f[0]
    api_start_index = 0
    title_start_index = 0
    for i in range(len(f)):
        line = f[i]
        if '===' in line and ('====') not in line and f'<tt>{api}</tt>' in line:
            api_start_index = i
            break
    for i in range(api_start_index, 0, -1):
        line = f[i]
        if '==' in line and '===' not in line:
            title_start_index = i
            break
    title_end_index = api_start_index
    for i in range(title_start_index + 1, api_start_index, 1):
        line = f[i]
        if ('===' in line and ('====') not in line) or (
            '==' in line and ('===') not in line
        ):
            title_end_index = i
            break
    title = ''.join(f[title_start_index:title_end_index])
    api_end_index = len(f)
    for i in range(api_start_index + 1, len(f), 1):
        line = f[i]
        if ('===' in line and ('====') not in line) or (
            '==' in line and ('===') not in line
        ):
            api_end_index = i
            break
    api_doc = ''.join(f[api_start_index:api_end_index])
    return title + api_doc


def initialize_session():
    """Initialize the session for HTTP requests."""
    import requests
    from bs4 import BeautifulSoup

    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:9999'
    # create a session and login
    s = requests.Session()
    r = s.get(f'{BASE_URL}/login')
    soup = BeautifulSoup(r.content, 'html.parser')
    csrf_token = soup.find('input', attrs={'name': '_csrf_token'})['value']

    payload = {
        '_csrf_token': csrf_token,
        '_username': 'MarvelsGrantMan136',
        '_password': 'test1234',
        '_remember_me': 'on',
    }

    s.post(f'{BASE_URL}/login_check', data=payload)
    return s


# Move all the API functions into a class to prevent them from running on import
class MapAPI:
    def __init__(self):
        self.s = initialize_session()
        self.BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:9999'

    def subscribe_forum(self, forum_name):
        # forum_name: str, forum_name, e.g. "relationship_advice"
        r = self.s.get(f'{self.BASE_URL}/f/{forum_name}')
        soup = BeautifulSoup(r.content, 'html.parser')

        csrf_token = soup.find('form', {'class': 'subscribe-form'}).find(
            'input', attrs={'name': 'token'}
        )['value']

        r = self.s.post(
            f'{self.BASE_URL}/f/{forum_name}/subscribe.json',
            files=dict(token=(None, csrf_token)),
        )
        return r.json()

    # ... rest of the API methods ...


# Create a global instance that can be used by other functions
map_api = None


def get_map_api():
    global map_api
    if map_api is None:
        map_api = MapAPI()
    return map_api
