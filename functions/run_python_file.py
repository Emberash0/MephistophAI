import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:    
        abs_working_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_working_path, file_path))

        valid_target_dir = os.path.commonpath([abs_working_path, target_path]) == abs_working_path
        if not valid_target_dir:
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        
        if not os.path.isfile(target_path):
            raise Exception(f'Error: "{file_path}" does not exist or is not a regular file')
        if target_path[-3:] != ".py":
            raise Exception(f'Error: "{file_path}" is not a Python file')
        
        command = ["python", target_path]
        if args:
            command.extend(args)

        python_run = subprocess.run(command, text=True, capture_output=True, timeout=30, cwd=abs_working_path)

        return_string = f""
        if python_run.returncode != 0:
            return_string += f"Process exited with code {python_run.returncode}\n"
        if python_run.stdout == None and python_run.stderr == None:
            return_string += f"No output produced"
        else:
            if python_run.stdout != "":
                return_string += f"STDOUT: {python_run.stdout}"
            if python_run.stderr != "":
                return_string += f"\nSTDERR: {python_run.stderr}"
        return return_string
    except Exception as e:
        print(f"Error: executing python file: {e}")






