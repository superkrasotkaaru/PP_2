import os

def delete_file(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            print(f"The file '{file_path}' exists.")

            # Check if the file is writable
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"The file '{file_path}' has been successfully deleted.")
            else:
                print(f"The file '{file_path}' is not writable. Cannot delete.")
        else:
            print(f"The file '{file_path}' does not exist. Cannot delete.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the file you want to delete
file_to_delete = "/path/to/your/file_to_delete.txt"

# Call the function to delete the file
delete_file(file_to_delete)
