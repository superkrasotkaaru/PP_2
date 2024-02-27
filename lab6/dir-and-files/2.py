import os

def check_path_access(path):
    # Check existence
    if os.path.exists(path):
        print(f"{path} exists.")
        
        # Check readability
        if os.access(path, os.R_OK):
            print(f"{path} is readable.")
        else:
            print(f"{path} is not readable.")

        # Check writability
        if os.access(path, os.W_OK):
            print(f"{path} is writable.")
        else:
            print(f"{path} is not writable.")

        # Check executability
        if os.access(path, os.X_OK):
            print(f"{path} is executable.")
        else:
            print(f"{path} is not executable.")
    else:
        print(f"{path} does not exist.")

# Specify the path you want to check
path_to_check = "/path/to/your/directory_or_file"

# Call the function to check access
check_path_access(path_to_check)
