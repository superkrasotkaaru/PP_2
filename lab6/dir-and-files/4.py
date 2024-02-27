def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The file '{file_path}' has {line_count} lines.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the text file
file_path = "/path/to/your/text_file.txt"

# Call the function to count lines
count_lines(file_path)
