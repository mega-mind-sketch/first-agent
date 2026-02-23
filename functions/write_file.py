import os

def write_file(working_directory, file_path, content):
    working_abs_dir = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_abs_dir, file_path))
    validate_file_path = os.path.commonpath([working_abs_dir, target_file_path]) == working_abs_dir

    try:

        if not validate_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            if not os.path.exists(target_file_path):
                os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

            with open(target_file_path, 'w') as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
