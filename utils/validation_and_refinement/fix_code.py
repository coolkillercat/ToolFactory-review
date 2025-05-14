# code agent

import anthropic  


def initialize_claude():
    """Initialize the Claude API client"""
    # $env:ANTHROPIC_API_KEY='your-key-here'
    client = anthropic.Anthropic()
    return client

def fix_code(client, code: str, error: str, api_doc: str, params: dict) -> str:
    """Fix code using Claude API with structured instructions"""
    
    with open("./template/fix_code_prompt_template.txt", "r") as f:
        template = f.read()

    prompt = template.format(client=client, code=code, error=error, api_doc=api_doc, params=str(params))

    chat = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=2048,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    try:
        return chat.content[0].text.strip()
    except (AttributeError, IndexError) as e:
        raise RuntimeError("Failed to process API response") from e