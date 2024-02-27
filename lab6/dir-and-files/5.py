def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"The list has been successfully written to the file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the file
file_path = "/path/to/your/output_file.txt"

# Specify the list to be written to the file
my_list = [1, 2, 3, 4, 5, "Hello", "World"]

# Call the function to write the list to the file
write_list_to_file(file_path, my_list)
