"""
GPT evaluator for API responses.
Uses GPT to determine if an API response is information or an error message.
"""

from langchain.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
import json


# Define the model for classification output
class Classification(BaseModel):
    """Classification output model."""
    response_type: str = Field(..., enum=['information', 'error'])


def initialize_gpt_evaluator(temperature=0, model="gpt-4o-mini"):
    """
    Initialize the GPT evaluator.
    
    Args:
        temperature: Temperature parameter for the model
        model: The model name to use
        
    Returns:
        llm: The initialized LLM
        tagging_prompt: The prompt template
    """
    # Create prompt template
    tagging_prompt = ChatPromptTemplate.from_template(
        """
        Decide if the following API response is an information or an error message.

        API Description:
        {description}
        API Response:
        {response}
        """
    )
    
    # Initialize LLM
    llm = ChatOpenAI(temperature=temperature, model=model).with_structured_output(Classification)
    
    return llm, tagging_prompt


def gpt_evaluate(llm, prompt_template, api_description, api_response):
    """
    Use GPT to decide if the API response is a piece of information or an error message.
    
    Args:
        llm: The LLM to use
        prompt_template: The prompt template
        api_description: Description of the API
        api_response: The API response to evaluate
        
    Returns:
        response_type: 'information' or 'error'
    """
    # Truncate the response to avoid token limit issues
    if isinstance(api_response, str):
        api_response = api_response[:500] if len(api_response) > 500 else api_response
    
    # Invoke the prompt
    prompt = prompt_template.invoke({
        "description": api_description, 
        "response": api_response
    })
    
    # Get the response from GPT
    gpt_response = llm.invoke(prompt)
    
    return gpt_response.response_type


def validate_test_results(apidocs_dir, max_file_size=100*1024*1024):
    """
    Validate the test results using GPT.
    
    Args:
        apidocs_dir: Directory containing API docs
        max_file_size: Maximum file size to process (in bytes)
        
    Returns:
        stats: Statistics about the validation
    """
    # Initialize GPT evaluator
    llm, tagging_prompt = initialize_gpt_evaluator()
    
    # Statistics
    stats = {
        'count_single_param_files': 0,
        'count_multi_param_files': 0,
        'count_validated_files': 0,
        'count_validated_single_param_files': 0,
        'count_validated_multi_param_files': 0,
        'count_find_by_semantic': 0,
        'count_find_by_semantic_single': 0,
        'count_find_by_semantic_multi': 0,
        'semantic_cases': []
    }
    
    # List all the folders
    folders = os.listdir(apidocs_dir)
    
    for folder in folders:
        files = os.listdir(os.path.join(apidocs_dir, folder))
        files = [x for x in files if x.endswith("_example_test.json")]
        
        for file_name in files:
            file_path = os.path.join(apidocs_dir, folder, file_name)
            
            # Skip large files
            if os.path.getsize(file_path) > max_file_size:
                continue
                
            # Load the test results
            endpoint_result = json.load(open(file_path))
            endpoint_result['validated_parameters'] = {}
            
            print(f"Validating {folder}.{endpoint_result['endpoint']}")
            
            # Track seen error responses to avoid repeating evaluation
            saved_error_responses = set()
            
            # Count files by parameter type
            if endpoint_result['tests']:
                if type(endpoint_result['tests'][0]['gt_param']) == str:
                    stats['count_single_param_files'] += 1
                else:
                    stats['count_multi_param_files'] += 1
                    
            # Evaluate each test
            for test in endpoint_result['tests']:
                status_code = test['status_code']
                
                if status_code == 200:
                    response_text = test['text']
                    
                    # Skip if we've already seen this response text
                    if response_text in saved_error_responses:
                        continue
                        
                    # Evaluate the response
                    gpt_response = gpt_evaluate(llm, tagging_prompt, endpoint_result['endpoint'], response_text)
                    
                    if gpt_response == 'error':
                        print(f"Error response detected: {response_text}")
                        saved_error_responses.add(response_text)
                    else:
                        print(f"Information response detected: {response_text}")
                        stats['count_validated_files'] += 1
                        
                        # Handle single parameter case
                        if type(test['gt_param']) == str:
                            endpoint_result['validated_parameters'][test['gt_param']] = test['candidate']
                            stats['count_validated_single_param_files'] += 1
                            
                            if not test['test_param'] in endpoint_result['extracted_parameters']:
                                stats['count_find_by_semantic'] += 1
                                stats['count_find_by_semantic_single'] += 1
                                stats['semantic_cases'].append((folder, endpoint_result['endpoint'], test['test_param'], test['gt_param']))
                        # Handle multi parameter case
                        else:
                            stats['count_validated_multi_param_files'] += 1
                            
                            for i, gt_param in enumerate(test['gt_param']):
                                endpoint_result['validated_parameters'][gt_param] = test['candidate'][i]
                                
                                if not test['test_param'][i] in endpoint_result['extracted_parameters']:
                                    stats['count_find_by_semantic'] += 1
                                    stats['count_find_by_semantic_multi'] += 1
                                    stats['semantic_cases'].append((folder, endpoint_result['endpoint'], test['test_param'][i], gt_param))
                        break
                        
            # Save the updated results
            with open(file_path, "w") as f:
                json.dump(endpoint_result, f)
                
    # Print statistics
    print(f"Validated {stats['count_validated_files']} parameters in "
          f"{stats['count_multi_param_files'] + stats['count_single_param_files']} files. "
          f"{stats['count_find_by_semantic']} parameters are found by semantic search.")
    
    print(f"Validated {stats['count_validated_single_param_files']} single parameters in "
          f"{stats['count_single_param_files']} files. "
          f"{stats['count_find_by_semantic_single']} single parameters are found by semantic search.")
    
    print(f"Validated {stats['count_validated_multi_param_files']} multi parameters in "
          f"{stats['count_multi_param_files']} files. "
          f"{stats['count_find_by_semantic_multi']} multi parameters are found by semantic search.")
    
    return stats 