import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    path = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(path, directory))
    
    if os.path.isfile(target_file) == False:
        raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')
    
    valid_target_file = os.path.commonpath([path, target_file]) == path
    
    if not valid_target_file:
        raise Exception(f'Error: Cannot read "{file_path}" as it is outside permitted working directory')

    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'