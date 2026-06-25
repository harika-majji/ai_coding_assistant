import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path: str, args = []):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path)) 
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not file_path.endswith(".py"):
        return f'Error "{file_path}" is not a python file'
    
    try:
        final_args = ["python3",file_path]
        final_args.extend(args)
        output = subprocess.run(final_args,cwd = abs_working_directory,timeout=300, capture_output=True)
        finalOutput =  f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
            """
    
        if output.stdout== "" or output.stderr == "":
            finalOutput = "No output produced.\n"

        if output.returncode !=0:
            finalOutput += f' Process Exited with code: {output.returncode}'

        return finalOutput
    except Exception as e:
        return f'Error executing python file: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description = "Runs a python file with the python3 interpreter. Accepts additional CLI args as an optional array.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The file to run, relative to the working directory."
            ),
            "args": types.Schema(
                type = types.Type.ARRAY,
                description = "An optional array of strings to be used as the CLI args for the python file.",
                items = types.Schema(
                    type = types.Type.STRING
                )
            )
        }
    )
)