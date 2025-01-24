import json
import yaml
import re
from urllib.parse import urlparse, urljoin
import sys
import os
from collections import defaultdict

def sanitize_operation_id(method, path):
    # Remove braces and angle brackets
    sanitized_path = re.sub(r'[{}<>]', '', path)
    # Replace slashes with underscores
    sanitized_path = sanitized_path.replace('/', '_')
    # Remove leading/trailing underscores
    sanitized_path = sanitized_path.strip('_')
    # Replace spaces with underscores
    sanitized_path = sanitized_path.replace(' ', '_')
    # Combine method and path
    operation_id = f"{method}_{sanitized_path}"
    # Replace any remaining invalid characters
    operation_id = re.sub(r'\W+', '_', operation_id)
    return operation_id

def process_parameters(parameters_list, path_parameters, required):
    parameters = []
    for param in parameters_list:
        # Replace spaces in parameter names with underscores
        param_name = param['name'].replace(' ', '_')
        if param_name in path_parameters:
            param_in = 'path'
            required_flag = True
        else:
            param_in = 'query'
            required_flag = required

        parameter = {
            'name': param_name,
            'in': param_in,
            'required': required_flag,
            'schema': {
                'type': param.get('type', 'string')
            },
            'description': param.get('description', '')
        }
        if param.get('default') is not None:
            parameter['schema']['default'] = param['default']
        if param.get('example') is not None:
            parameter['example'] = param['example']

        parameters.append(parameter)
    return parameters

def process_endpoint(endpoint, base_path):
    method = endpoint['method'].lower()
    url = endpoint['url']
    description = endpoint.get('description', '')
    summary = endpoint.get('name', '')

    # Parse the URL
    if isinstance(url, list):
        url = url[0]
    parsed_url = urlparse(url)
    path = parsed_url.path

    # Replace spaces in parameter names with underscores before processing
    path = re.sub(r'<([^<>]+)>', lambda m: '<' + m.group(1).replace(' ', '_') + '>', path)

    # Replace ":param", "{param}", or "<param>" with "{param}"
    # Handle parameters with spaces replaced by underscores
    path = re.sub(r':(\w+)', r'{\1}', path)
    path = re.sub(r'\{([^{}]+)\}', lambda m: '{' + m.group(1).replace(' ', '_') + '}', path)
    path = re.sub(r'<([^<>]+)>', r'{\1}', path)

    # Remove base path from path
    if path.startswith(base_path):
        path = path[len(base_path):]
        if not path.startswith('/'):
            path = '/' + path

    # Extract path parameters
    path_parameters = re.findall(r'{([^{}]+)}', path)

    # Initialize the operation
    operation = {
        'operationId': sanitize_operation_id(method, path),
        'summary': summary,
        'description': description,
        'parameters': [],
        'responses': {
            '200': {
                'description': 'Success'
            }
        }
    }

    # Process parameters
    required_parameters = endpoint.get('required_parameters', [])
    optional_parameters = endpoint.get('optional_parameters', [])
    if not required_parameters:
        required_parameters = []
    if not optional_parameters:
        optional_parameters = []
    operation['parameters'].extend(process_parameters(required_parameters, path_parameters, required=True))
    operation['parameters'].extend(process_parameters(optional_parameters, path_parameters, required=False))

    return path, method, operation

def merge_openapi_specs(spec1, spec2):
    # Merge paths
    for path, methods in spec2.get('paths', {}).items():
        if path not in spec1['paths']:
            spec1['paths'][path] = methods
        else:
            for method, operation in methods.items():
                spec1['paths'][path][method] = operation

    return spec1

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_openapi.py [input_directory]")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = "./yamloutput"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Dictionary to hold OpenAPI specs per domain
    domain_specs = {}

    # Walk through the main directory and process all .txt files in subfolders
    for root, dirs, files in os.walk(input_dir):
        config = {}
        # Check for .config file in the current directory
        config_file = os.path.join(root, '.config')
        if os.path.isfile(config_file):
            with open(config_file, 'r') as cf:
                try:
                    config = json.load(cf)
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON in config file {config_file}: {e}")

        base_url = config.get('base_url', '')

        for file in files:
            if file.endswith('.txt'):
                input_file = os.path.join(root, file)
                with open(input_file, 'r') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError as e:
                        print(f"Error parsing JSON in file {input_file}: {e}")
                        continue

                title = data.get('title', 'API Documentation')
                endpoints = data.get('endpoints', [])
                if not endpoints:
                    print(f"No endpoints found in {input_file}.")
                    continue

                # Prepend base_url to all endpoint URLs if base_url is provided
                for endpoint in endpoints:
                    endpoint_url = endpoint['url']
                    if base_url:
                        endpoint_url = urljoin(base_url, endpoint_url)
                        endpoint['url'] = endpoint_url

                # Determine the base URL for this set of endpoints
                first_url = endpoints[0]['url']
                if isinstance(first_url, list):
                    first_url = first_url[0] 
                parsed_url = urlparse(first_url)
                if not parsed_url.scheme:
                    # Default to http if scheme is missing
                    parsed_url = parsed_url._replace(scheme='http')
                base_url_full = f"{parsed_url.scheme}://{parsed_url.netloc}"

                base_path = ''  # Base path can be customized if needed

                # Initialize OpenAPI spec for this subfolder
                openapi_spec_subfolder = {
                    'openapi': '3.1.0',  # Updated OpenAPI version
                    'info': {
                        'title': title,
                        'version': '1.0.0',
                    },
                    'servers': [
                        {
                            'url': base_url_full
                        }
                    ],
                    'paths': {},
                }

                # Initialize or retrieve the OpenAPI spec for the domain (for merged files)
                if base_url_full not in domain_specs:
                    domain_specs[base_url_full] = {
                        'openapi': '3.1.0',  # Updated OpenAPI version
                        'info': {
                            'title': f"API Documentation for {base_url_full}",
                            'version': '1.0.0',
                        },
                        'servers': [
                            {
                                'url': base_url_full
                            }
                        ],
                        'paths': {},
                    }

                openapi_spec_domain = domain_specs[base_url_full]

                # Process each endpoint
                for endpoint in endpoints:
                    path, method, operation = process_endpoint(endpoint, base_path)
                    # Add to subfolder OpenAPI spec
                    if path not in openapi_spec_subfolder['paths']:
                        openapi_spec_subfolder['paths'][path] = {}
                    openapi_spec_subfolder['paths'][path][method] = operation
                    # Add to domain OpenAPI spec (for merged files)
                    if path not in openapi_spec_domain['paths']:
                        openapi_spec_domain['paths'][path] = {}
                    openapi_spec_domain['paths'][path][method] = operation

                # Write OpenAPI spec to openapi.yaml in the subfolder
                output_file_subfolder = os.path.join(root, 'openapi.yaml')
                with open(output_file_subfolder, 'w') as f:
                    yaml.dump(openapi_spec_subfolder, f, sort_keys=False)
                print(f"OpenAPI YAML file generated in subfolder: {output_file_subfolder}")

    # Write the merged OpenAPI specs to YAML files per domain in the output directory
    for base_url_full, spec in domain_specs.items():
        domain_name = urlparse(base_url_full).netloc.replace(':', '_')
        output_file = os.path.join(output_dir, f"{domain_name}.yaml")
        # If the file exists, merge the specs
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                existing_spec = yaml.safe_load(f)
            spec = merge_openapi_specs(existing_spec, spec)

        with open(output_file, 'w') as f:
            yaml.dump(spec, f, sort_keys=False)
        print(f"OpenAPI YAML file generated for domain {base_url_full}: {output_file}")

if __name__ == "__main__":
    main()
