import os

def list_directories(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def list_files(path):
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all_items(path):
    print("\nAll Directories and Files:")
    for item in os.listdir(path):
        print(item)

# Specify the path you want to list
path_to_list = "/path/to/your/directory"

# Call the functions to list directories, files, and all items
list_directories(path_to_list)
list_files(path_to_list)
list_all_items(path_to_list)
