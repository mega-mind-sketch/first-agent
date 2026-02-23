import os
import subprocess



def run_python_file(working_directory, file_path, args=None):

    working_abs_dir = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_abs_dir, file_path))
    validate_file_path = os.path.commonpath([working_abs_dir, target_file_path]) == working_abs_dir

    try:
        if not validate_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif not target_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file_path]

        if args:
            command.extend(args)
        
        
        result = subprocess.run(
            command,
            cwd=working_abs_dir,
            capture_output=True,
            text=True,
            timeout=30, 
            )
    
        output = []

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        if result.stdout:
            output.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr}")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"