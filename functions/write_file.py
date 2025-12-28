import os

def write_file(working_directory, file_path, content):
    path = os.path.abspath(working_directory)
    file_list = file_path.split("/")
    target_file = os.path.normpath(os.path.join(path, "/".join(file_list[:-1])))

    valid_target_file = os.path.commonpath([path, target_file]) == path    
    if not valid_target_file:
        raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    os.makedirs(target_file, exist_ok=True)
    
    file_name = file_list[-1]
    target_file = os.path.normpath(os.path.join(target_file, file_name))
    if os.path.isdir(target_file):
        raise Exception(f'Error: Cannot write to "{file_path}" as it is a directory')

    with open(target_file, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'