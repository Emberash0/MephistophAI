import os

def get_files_info(working_directory, directory="."):
    
    path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(path, directory))
    
    if os.path.isdir(target_dir) == False:
        raise Exception(f'Error: "{directory}" is not a directory')
    
    valid_target_dir = os.path.commonpath([path, target_dir]) == path
    
    if not valid_target_dir:
        raise Exception(f'Error: Cannot list "{directory}" as it is outside permitted working directory')
    
    result = []
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        result.append(
            f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
        )
    return "\n".join(result)