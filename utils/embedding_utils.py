"""
Embedding utilities for semantic search of parameters and API responses.
"""

import random
from sentence_transformers import SentenceTransformer, util


def initialize_model(model_name="flax-sentence-embeddings/st-codesearch-distilroberta-base"):
    """
    Initialize the sentence transformer model for embeddings.
    
    Args:
        model_name: Name of the pretrained model to use
        
    Returns:
        model: Initialized SentenceTransformer model
    """
    return SentenceTransformer(model_name)


def encode_keys(model, keys_dict):
    """
    Encode dictionary keys using the sentence transformer model.
    
    Args:
        model: SentenceTransformer model
        keys_dict: Dictionary of keys to encode
        
    Returns:
        keys: List of keys
        keys_emb: Tensor of encoded keys
    """
    keys = list(keys_dict.keys())
    keys_emb = model.encode(keys, convert_to_tensor=True)
    return keys, keys_emb


def get_test_examples(
    query, 
    api_doc_name, 
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
    max_param_examples=5, 
    max_response_examples=5, 
    max_examples_per_hit=1, 
    similarity_threshold=0.5
):
    """
    Get test examples for a parameter based on semantic search.
    
    Args:
        query: Parameter name to search for
        api_doc_name: Name of the API doc
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
        max_param_examples: Maximum number of parameter examples to return
        max_response_examples: Maximum number of response examples to return
        max_examples_per_hit: Maximum number of examples per hit
        similarity_threshold: Threshold for similarity score
        
    Returns:
        all_examples: Set of parameter examples
    """
    query_description = None
    if param_to_description_dict:
        try:
            query_description = param_to_description_dict[query]
        except:
            query_description = None
            
    query_emb = model.encode(query, convert_to_tensor=True) 
    hits_param = util.semantic_search(query_emb, param_keys_emb)
    hits_response = util.semantic_search(query_emb, response_keys_emb)
    
    all_examples = set()
    
    # Process parameter hits
    hit_list = hits_param[0]
    count = 0
    for hit in hit_list:
        if hit['score'] < similarity_threshold or count >= max_param_examples:
            break
        param_key = param_keys[hit['corpus_id']]
        examples_set = parameter_dict[param_key]
        filtered_examples = [t[1] for t in examples_set if t[0] != api_doc_name]
        examples = random.sample(filtered_examples, min(len(filtered_examples), max_examples_per_hit))
        sidx = param_key.rfind('[')+1
        test_param = param_key[sidx:-1]
        pairs = [(test_param, example) for example in examples]
        all_examples.update(pairs)
        count += len(examples)
    
    # Process response hits
    hit_list = hits_response[0]
    count = 0
    for hit in hit_list:
        if hit['score'] < similarity_threshold or count >= max_response_examples:
            break
        response_key = response_keys[hit['corpus_id']]
        examples_set = response_dict[response_key]
        filtered_examples = [t[1] for t in examples_set if t[0] != api_doc_name]
        examples = random.sample(filtered_examples, min(len(filtered_examples), max_examples_per_hit))
        sidx = response_key.rfind('[')+1
        test_param = response_key[sidx:-1]
        pairs = [(test_param, example) for example in examples]
        all_examples.update(pairs)
        count += len(examples)
    
    # Process description hits if available
    if query_description and description_keys and description_keys_emb and description_to_param_dict:
        query_description_emb = model.encode(query_description, convert_to_tensor=True)
        hits_description = util.semantic_search(query_description_emb, description_keys_emb)
        hit_list = hits_description[0]
        count = 0
        for hit in hit_list:
            if hit['score'] < similarity_threshold or count >= max_param_examples:
                break
            description_key = description_keys[hit['corpus_id']]
            param_key = description_to_param_dict[description_key]
            examples_set = parameter_dict['['+param_key+']']
            filtered_examples = [t[1] for t in examples_set if t[0] != api_doc_name]
            examples = random.sample(filtered_examples, min(len(filtered_examples), max_examples_per_hit))
            pairs = [(param_key, example) for example in examples]
            all_examples.update(pairs)
            count += len(examples)
            
    return all_examples 