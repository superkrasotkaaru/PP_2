import os

def analyze_path(path):
    # Check if the path exists
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        # Extract filename and directory portions
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")

# Specify the path you want to analyze
path_to_analyze = "/path/to/your/file_or_directory"

# Call the function to analyze the path
analyze_path(path_to_analyze)
