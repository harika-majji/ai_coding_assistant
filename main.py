import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_function import call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
  
    print(sys.argv)

    if len(sys.argv)<2:
        print("I need a prompt")
        return
    system_prompt ="""
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read the contents of a file.
        - Write to a file (create or update)
        - Run a Python file with optional arguments

        When the user asks about the code project - they are referring to the working directory. So, you should start by looking ar the project's files, and figuring out how to run the project and how to run its tests, you'll always want to test the tests and the actual project to verify that behaviour is working.
        All paths you provide should be relative to the working directory. 
        You do need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """
    prompt = sys.argv[1]
    client = genai.Client(api_key = api_key)

    messages = [
        types.Content(role = "user",parts = [types.Part(text=prompt)])
        ]
    
    available_functions = types.Tool(
        function_declarations = [schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
    )
    config = types.GenerateContentConfig(
        tools = [available_functions],
        system_instruction=system_prompt)
    
    max_iter = 20
    for i in range(0, max_iter):
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config = config
        )

        if response is None or response.usage_metadata is None:
            print("response is malformed")
            return
        
        print("User prompt", prompt)
        print("Prompt Tokens", response.usage_metadata.prompt_token_count)
        print("Output token",response.usage_metadata.candidates_token_count)
        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)
        if response.function_calls:
            for function_call_part in response.function_calls:
                result = call_function(function_call_part)
                messages.append(result)
        else:
            print(response.text)
            return

    
main()