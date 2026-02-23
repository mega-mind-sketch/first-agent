import os



def get_files_info(working_directory, directory="."):
    
    working_dir_abs = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))


    validate_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    # if directory == ".":
    #     print("Result for current directory:")
    # else:
    #     print(f"Result for '{directory}' directory:")
    
    try:

        if not validate_target_dir:
            return f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'\tError: "{directory}" is not a directory'
        else:
            output = []
            with os.scandir(target_dir) as entries:
                for entry in entries:
                    output.append(f'\t- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}')
            
            return "\n".join(output)
    except Exception as e:
        return f"Error: {e}"