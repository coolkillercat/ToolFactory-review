"""
Tool testing utilities for running experiments on generated API tools.
"""

import os
import json
import time
import inspect
import random
import itertools
import subprocess


def load_and_import(api_name, function_name):
    """
    Dynamically load and import a generated API tool.
    
    Args:
        api_name: Name of the API
        function_name: Name of the function to import
        
    Returns:
        module: Imported module
    """
    import sys
    folder_path = os.path.join("..", "extractor", "apidocs", api_name)
    sys.path.insert(0, folder_path)
    module = __import__(function_name)
    sys.path.pop(0)  # Clean up after import
    return module


def get_function(api_name, endpoint_name):
    """
    Get a function from a generated API tool.
    
    Args:
        api_name: Name of the API
        endpoint_name: Name of the endpoint
        
    Returns:
        function: The function
    """
    function_name = endpoint_name.replace("_GET", "").replace("_POST", "")
    module = load_and_import(api_name, endpoint_name)
    f = getattr(module, function_name)
    return f


def get_parameter_names(func):
    """
    Get the parameter names of a function.
    
    Args:
        func: The function
        
    Returns:
        parameter_names: List of parameter names
    """
    signature = inspect.signature(func)
    return [param.name for param in signature.parameters.values()]


def test_api_call(api_name, endpoint_name, parameter_values):
    """
    Test an API call with given parameter values.
    
    Args:
        api_name: Name of the API
        endpoint_name: Name of the endpoint
        parameter_values: Dictionary of parameter values
        
    Returns:
        response: API response or None if error
    """
    try:
        f = get_function(api_name, endpoint_name)
        response = f(**parameter_values)
        return response
    except Exception as e:
        print(f'Error occurred when calling {api_name}.{endpoint_name} with {parameter_values}: {str(e)}')
        return None


def execute_api_script(file_path):
    """
    Execute an API script and capture the output.
    
    Args:
        file_path: Path to the API script
        
    Returns:
        output_json: Output JSON or None if error
    """
    try:
        result = subprocess.run(
            ["python", file_path], capture_output=True, text=True, check=True
        )
        if result.stdout:
            output = result.stdout
            output_json = json.loads(output)
            return output_json
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f'Error executing {file_path}: {str(e)}')
        return None


def test_single_parameter_endpoint(
    folder, 
    endpoint_name, 
    get_test_examples_func, 
    model,
    param_keys, 
    param_keys_emb, 
    parameter_dict, 
    response_keys, 
    response_keys_emb, 
    response_dict,
    description_keys=None, 
    description_keys_emb=None, 
    description_to_param_dict=None, 
    param_to_description_dict=None,
    sleep_time=0.1
):
    """
    Test an endpoint with a single parameter.
    
    Args:
        folder: Name of the API folder
        endpoint_name: Name of the endpoint
        get_test_examples_func: Function to get test examples
        model: SentenceTransformer model
        param_keys: List of parameter keys
        param_keys_emb: Encoded parameter keys
        parameter_dict: Dictionary of parameters
        response_keys: List of response keys
        response_keys_emb: Encoded response keys
        response_dict: Dictionary of responses
        description_keys: List of description keys
        description_keys_emb: Encoded description keys
        description_to_param_dict: Dictionary mapping descriptions to parameter names
        param_to_description_dict: Dictionary mapping parameter names to descriptions
        sleep_time: Time to sleep between API calls
        
    Returns:
        tests: List of test results
    """
    f = get_function(folder, endpoint_name)
    param_names = get_parameter_names(f)
    tests = []
    
    if len(param_names) == 1:
        curr_param = param_names[0]
        examples = get_test_examples_func(
            curr_param, 
            folder, 
            model,
            param_keys, 
            param_keys_emb, 
            parameter_dict, 
            response_keys, 
            response_keys_emb, 
            response_dict,
            description_keys, 
            description_keys_emb, 
            description_to_param_dict, 
            param_to_description_dict
        )
        
        for test_param, example in examples:
            try:
                response = f(example)
            except Exception as e:
                print(f'Error occurred when calling {folder}.{endpoint_name} with {curr_param}={example}: {str(e)}')
                continue
                
            response_json = ""
            try:
                response_json = response.json()
            except:
                pass
                
            example_result = {
                'gt_param': curr_param,
                'test_param': test_param, 
                'candidate': example, 
                'status_code': response.status_code, 
                'json': response_json, 
                'text': response.text
            }
            tests.append(example_result)
            time.sleep(sleep_time)
    
    return tests


def test_multi_parameter_endpoint(
    folder, 
    endpoint_name, 
    get_test_examples_func, 
    model,
    param_keys, 
    param_keys_emb, 
    parameter_dict, 
    response_keys, 
    response_keys_emb, 
    response_dict,
    description_keys=None, 
    description_keys_emb=None, 
    description_to_param_dict=None, 
    param_to_description_dict=None,
    max_samples=100,
    sleep_time=0.1
):
    """
    Test an endpoint with multiple parameters.
    
    Args:
        folder: Name of the API folder
        endpoint_name: Name of the endpoint
        get_test_examples_func: Function to get test examples
        model: SentenceTransformer model
        param_keys: List of parameter keys
        param_keys_emb: Encoded parameter keys
        parameter_dict: Dictionary of parameters
        response_keys: List of response keys
        response_keys_emb: Encoded response keys
        response_dict: Dictionary of responses
        description_keys: List of description keys
        description_keys_emb: Encoded description keys
        description_to_param_dict: Dictionary mapping descriptions to parameter names
        param_to_description_dict: Dictionary mapping parameter names to descriptions
        max_samples: Maximum number of samples to test
        sleep_time: Time to sleep between API calls
        
    Returns:
        tests: List of test results
    """
    f = get_function(folder, endpoint_name)
    param_names = get_parameter_names(f)
    tests = []
    
    if len(param_names) > 1:
        example_list = []
        for param in param_names:
            examples = get_test_examples_func(
                param, 
                folder, 
                model,
                param_keys, 
                param_keys_emb, 
                parameter_dict, 
                response_keys, 
                response_keys_emb, 
                response_dict,
                description_keys, 
                description_keys_emb, 
                description_to_param_dict, 
                param_to_description_dict
            )
            example_list.append(examples)
            
        candidate_combinations = list(itertools.product(*example_list))
        samples = random.sample(candidate_combinations, min(max_samples, len(candidate_combinations)))
        
        for sample in samples:
            try:
                input_dict = {param_names[i]: sample[i][1] for i in range(len(param_names))}
                response = f(**input_dict)
            except Exception as e:
                print(f'Error occurred when calling {folder}.{endpoint_name} with {input_dict}: {str(e)}')
                continue
                
            response_json = ""
            try:
                response_json = response.json()
            except:
                pass
                
            example_result = {
                'gt_param': param_names,
                'test_param': [t[0] for t in sample], 
                'candidate': [t[1] for t in sample], 
                'status_code': response.status_code, 
                'json': response_json, 
                'text': response.text
            }
            tests.append(example_result)
            time.sleep(sleep_time)
    
    return tests


def run_experiment(
    apidocs_dir,
    get_test_examples_func,
    model,
    param_keys, 
    param_keys_emb, 
    parameter_dict, 
    response_keys, 
    response_keys_emb, 
    response_dict,
    description_keys=None, 
    description_keys_emb=None, 
    description_to_param_dict=None, 
    param_to_description_dict=None,
    max_samples=100,
    sleep_time=0.1
):
    """
    Run an experiment to test generated API tools.
    
    Args:
        apidocs_dir: Directory containing API docs
        get_test_examples_func: Function to get test examples
        model: SentenceTransformer model
        param_keys: List of parameter keys
        param_keys_emb: Encoded parameter keys
        parameter_dict: Dictionary of parameters
        response_keys: List of response keys
        response_keys_emb: Encoded response keys
        response_dict: Dictionary of responses
        description_keys: List of description keys
        description_keys_emb: Encoded description keys
        description_to_param_dict: Dictionary mapping descriptions to parameter names
        param_to_description_dict: Dictionary mapping parameter names to descriptions
        max_samples: Maximum number of samples to test
        sleep_time: Time to sleep between API calls
    """
    folders = os.listdir(apidocs_dir)
    for folder in folders:
        files = os.listdir(os.path.join(apidocs_dir, folder))
        files = [x for x in files if x.endswith(".py")]
        
        api_extracted_json = {}
        try:
            with open(os.path.join(apidocs_dir, folder, folder + ".txt")) as f:
                api_extracted_json = json.load(f)
        except:
            print(f"No extracted information for api: {folder}")
            continue
            
        extracted_endpoints = None
        try:
            extracted_endpoints = api_extracted_json['endpoints']
        except:
            print(f"No endpoints in extracted information for api: {folder}")
            continue
            
        for idx, file_name in enumerate(files):
            if file_name == "__init__.py":
                continue
                
            endpoint_name = file_name.replace(".py", "")
            record_file_name = endpoint_name + "_example_test.json"
            record_file_path = os.path.join(apidocs_dir, folder, record_file_name)
            
            if os.path.exists(record_file_path):
                endpoint_result = json.load(open(record_file_path))
            else:
                endpoint_result = {
                    "endpoint": endpoint_name, 
                    "tests": [], 
                    "extracted_parameters": {}, 
                    "validated_parameters": {}
                }
                print(f"Testing {folder}.{endpoint_name}")
                
                # Extract parameter information from the extracted endpoints
                current_endpoint = None
                for endpoint in extracted_endpoints:
                    current_endpoint_name = endpoint['name'].replace(' ','_').lower() + '_' + endpoint['method']
                    if current_endpoint_name == endpoint_name:
                        current_endpoint = endpoint
                        print(f"Found endpoint {endpoint_name} in extracted information")
                        break
                        
                if current_endpoint:
                    endpoint_result['extracted_parameters'] = {}
                    for req_param in current_endpoint['required_parameters']:
                        endpoint_result['extracted_parameters'][req_param['name']] = {
                            'description': req_param['description'], 
                            'example': req_param['example']
                        }
                    if current_endpoint['optional_parameters']:
                        for opt_param in current_endpoint['optional_parameters']:
                            endpoint_result['extracted_parameters'][opt_param['name']] = {
                                'description': opt_param['description'], 
                                'example': opt_param['example']
                            }
                
                # Test the endpoint
                try:
                    f = get_function(folder, endpoint_name)
                    param_names = get_parameter_names(f)
                    
                    if len(param_names) == 1:
                        tests = test_single_parameter_endpoint(
                            folder, 
                            endpoint_name, 
                            get_test_examples_func, 
                            model,
                            param_keys, 
                            param_keys_emb, 
                            parameter_dict, 
                            response_keys, 
                            response_keys_emb, 
                            response_dict,
                            description_keys, 
                            description_keys_emb, 
                            description_to_param_dict, 
                            param_to_description_dict,
                            sleep_time
                        )
                        endpoint_result['tests'] = tests
                    else:
                        tests = test_multi_parameter_endpoint(
                            folder, 
                            endpoint_name, 
                            get_test_examples_func, 
                            model,
                            param_keys, 
                            param_keys_emb, 
                            parameter_dict, 
                            response_keys, 
                            response_keys_emb, 
                            response_dict,
                            description_keys, 
                            description_keys_emb, 
                            description_to_param_dict, 
                            param_to_description_dict,
                            max_samples,
                            sleep_time
                        )
                        endpoint_result['tests'] = tests
                except Exception as e:
                    print(f"Error testing {folder}.{endpoint_name}: {str(e)}")
                
            # Save the results
            with open(record_file_path, "w") as f:
                json.dump(endpoint_result, f) 