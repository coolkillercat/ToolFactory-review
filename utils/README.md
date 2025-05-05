# Tool Testing Utilities

This folder contains utility functions for testing and evaluating generated API tools. These utilities help with building knowledge bases, performing semantic search for parameter values, testing endpoints, and evaluating responses.

## Setup

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Structure

- `kb_builder.py`: Functions for building knowledge bases from API docs
- `embedding_utils.py`: Utilities for embedding and semantic search
- `tool_tester.py`: Functions for testing generated tools
- `gpt_evaluator.py`: Utilities for evaluating API responses using GPT
- `main.py`: Example script demonstrating the use of the utilities

## Usage

### Running the Example

```bash
python main.py
```

This will:
1. Build knowledge bases from the API docs
2. Initialize embedding models
3. Run experiments to test the generated tools
4. Validate the test results using GPT

### Custom Usage

```python
import os
from utils.kb_builder import build_parameter_dict, build_description_dicts, build_response_dict
from utils.embedding_utils import initialize_model, encode_keys, get_test_examples
from utils.tool_tester import test_api_call
from utils.gpt_evaluator import initialize_gpt_evaluator, gpt_evaluate

# Define the path to the API docs
apidocs_dir = os.path.join("..", "extractor", "apidocs")

# Build knowledge bases
parameter_dict = build_parameter_dict(apidocs_dir)
description_to_param_dict, param_to_description_dict = build_description_dicts(apidocs_dir)
response_dict = build_response_dict(apidocs_dir)

# Initialize models
model = initialize_model()
param_keys, param_keys_emb = encode_keys(model, parameter_dict)
response_keys, response_keys_emb = encode_keys(model, response_dict)
description_keys, description_keys_emb = encode_keys(model, description_to_param_dict)

# Get example parameter values
examples = get_test_examples(
    "some_parameter", 
    "api_name", 
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

# Test an API call
response = test_api_call("api_name", "endpoint_name", {"param_name": "param_value"})

# Evaluate the response
llm, prompt_template = initialize_gpt_evaluator()
result = gpt_evaluate(llm, prompt_template, "API description", response.text)
```

## Utilities Overview

### KB Builder

- `build_parameter_dict`: Build a dictionary of parameters from API docs
- `build_description_dicts`: Build dictionaries mapping between parameter descriptions and names
- `build_response_dict`: Build a dictionary of API responses from saved response files

### Embedding Utils

- `initialize_model`: Initialize the sentence transformer model for embeddings
- `encode_keys`: Encode dictionary keys using the sentence transformer model
- `get_test_examples`: Get test examples for a parameter based on semantic search

### Tool Tester

- `load_and_import`: Dynamically load and import a generated API tool
- `get_function`: Get a function from a generated API tool
- `get_parameter_names`: Get the parameter names of a function
- `test_api_call`: Test an API call with given parameter values
- `execute_api_script`: Execute an API script and capture the output
- `test_single_parameter_endpoint`: Test an endpoint with a single parameter
- `test_multi_parameter_endpoint`: Test an endpoint with multiple parameters
- `run_experiment`: Run an experiment to test generated API tools

### GPT Evaluator

- `initialize_gpt_evaluator`: Initialize the GPT evaluator
- `gpt_evaluate`: Use GPT to decide if the API response is information or an error
- `validate_test_results`: Validate the test results using GPT 