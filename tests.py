from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_directory = "calculator"
    # root_contents = get_files_info(working_directory)
    # print(root_contents)
    # pkg_contents = get_files_info(working_directory, "pkg")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_directory, "/bin")
    # print(pkg_contents)

    # pkg_contents = get_files_info(working_directory, "../")
    # print(pkg_contents)

    # print(get_file_content(working_directory,"lorem.txt"))
    # print(get_file_content(working_directory, ".././main.py"))
    # print(get_file_content(working_directory, "pkg/calc.py"))
    # print(get_file_content(working_directory, "/bin/cat"))
    # print(get_file_content(working_directory, "pkg/does_not_exist.py"))
    
    print(write_file(working_directory, ".././lorem.txt", " Wait this is not the lorem file"))
    print(write_file(working_directory, "pkg/morelorem.txt", " New lorem file"))
    print(write_file(working_directory, "pkg2/morelorem.txt", " New lorem file"))
    print(write_file(working_directory, "/temp/temp.txt", "not allowed"))

    # print(run_python_file(working_directory, "main.py"))
    # print(run_python_file(working_directory, "main.py", ["3 + 5"]))
    # print(run_python_file(working_directory, "tests.py"))
    # print(run_python_file(working_directory, ".././main.py"))
    # print(run_python_file(working_directory, "lorem.py"))
    # print(run_python_file(working_directory, "lorem.txt"))
main()