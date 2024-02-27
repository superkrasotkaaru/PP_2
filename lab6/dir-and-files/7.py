def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
            content = source_file.read()
            destination_file.write(content)
        print(f"Contents of '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"One or both of the files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the paths for source and destination files
source_file_path = "/path/to/your/source_file.txt"
destination_file_path = "/path/to/your/destination_file.txt"

# Call the function to copy the contents
copy_file(source_file_path, destination_file_path)
