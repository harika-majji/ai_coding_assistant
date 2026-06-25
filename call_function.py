from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google.genai import types
working_directory = "calculator"
def call_function(functional_call_part, verbose = False):
    if verbose:
        print(f"Calling function : {functional_call_part.name}({functional_call_part.args})")

    else:
        print(f"- Calling function: {functional_call_part.name}")

    result = ""
    if functional_call_part.name == "get_files_info":
        result = get_files_info(working_directory, **functional_call_part.args)

    if functional_call_part.name == "get_file_content":
        result = get_file_content(working_directory, **functional_call_part.args)
    
    if functional_call_part.name == "write_file":
        result = write_file(working_directory, **functional_call_part.args)

    if functional_call_part.name == "run_python_file":
        result = run_python_file(working_directory, **functional_call_part.args)

    if result == "":

        return types.Content(
            role = "tool",
            parts = [
                types.Part.from_function_response(
                name = functional_call_part.name,
                response = {"error": f"Unknown function:"}
            )
            ],
        )
    return types.Content(
            role = "tool",
            parts = [types.Part.from_function_response(
                name = functional_call_part.name,
                response = { "result": result}, 
            )],
        )