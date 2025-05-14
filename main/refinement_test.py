import os
import json
import subprocess
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.validation_and_refinement.gpt_eval import (
    initialize_gpt_evaluator,
    gpt_evaluate,
)

apidocs_dir = os.path.join("extractor", "apidocs")
gpt, gpt_prompt = initialize_gpt_evaluator()

tool_success = 0
tool_code_error = 0
tool_server_error = 0
tool_hard_error = 0

# run the tools
print("Running tools...")
for tool_folder in os.listdir(apidocs_dir):
    # get the python tool scripts
    files = os.listdir(os.path.join(apidocs_dir, tool_folder))
    tools = [x for x in files if x.endswith(".py")]
    # get the api json file
    api_txt = [x for x in files if x.endswith(".txt")]
    api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0])))
    
    for tool in tools:
        tool_path = os.path.join(apidocs_dir, tool_folder, tool)
        code = open(tool_path, "r").read()
        try:
            result = subprocess.run(
                ["python", tool_path], capture_output=True, text=True, check=True
            )
            if result.stdout:
                output = result.stdout
                gpt_answer = gpt_evaluate(
                    gpt,
                    gpt_prompt,
                    api_description=api_json,
                    api_response=output,
                    code=code,
                )
                if gpt_answer == "code_error":
                    tool_code_error += 1
                    print(f"Tool {tool_path} returned a code error.")
                elif gpt_answer == "server_error":
                    tool_server_error += 1
                    print(f"Tool {tool_path} returned a server error.")
                elif gpt_answer == "information":
                    tool_success += 1
                    print(f"Tool {tool_path} executed successfully.")
                else:
                    print(f"Tool {tool_path} gpt answer: {gpt_answer}")
        # except subprocess.CalledProcessError as e:
        except Exception as e:
            tool_hard_error += 1
            print(f"Tool {tool_path} cannot be executed.")

print(
    f"Tool success: {tool_success}, Tool code error: {tool_code_error}, Tool server error: {tool_server_error}, Tool hard error: {tool_hard_error}"
)