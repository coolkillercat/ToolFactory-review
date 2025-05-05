"""
Main script to demonstrate how to use the tool testing utilities.
"""

import os
import sys
import json
from collections import defaultdict

# Add the parent directory to the path to import utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.kb_builder import (
    build_parameter_dict,
    build_description_dicts,
    build_response_dict
)
from utils.embedding_utils import (
    initialize_model,
    encode_keys,
    get_test_examples
)
from utils.tool_tester import (
    run_experiment
)
from utils.gpt_evaluator import (
    validate_test_results
)


def main():
    """
    Main function to run the tool testing utilities.
    """
    # Define the path to the API docs
    apidocs_dir = os.path.join("..", "extractor", "apidocs")
    
    print("Building knowledge bases...")
    # Build the parameter dictionary
    parameter_dict = build_parameter_dict(apidocs_dir)
    
    # Build the description dictionaries
    description_to_param_dict, param_to_description_dict = build_description_dicts(apidocs_dir)
    
    # Build the response dictionary
    response_dict = build_response_dict(apidocs_dir)
    
    print("Initializing embedding model...")
    # Initialize the embedding model
    model = initialize_model()
    
    # Encode the keys
    param_keys, param_keys_emb = encode_keys(model, parameter_dict)
    response_keys, response_keys_emb = encode_keys(model, response_dict)
    description_keys, description_keys_emb = encode_keys(model, description_to_param_dict)
    
    print("Running experiments...")
    # Run the experiments
    run_experiment(
        apidocs_dir,
        get_test_examples,
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
        max_samples=100,
        sleep_time=0.1
    )
    
    print("Validating test results...")
    # Validate the test results
    stats = validate_test_results(apidocs_dir)
    
    # Print the statistics
    print("Experiment complete!")
    print(f"Found {stats['count_find_by_semantic']} parameters using semantic search.")
    
    return stats


if __name__ == "__main__":
    main() 