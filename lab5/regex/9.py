import re

def insert_spaces(input_string):
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return modified_string

# Example usage:
input_string = "ThisIsCamelCaseString"
result = insert_spaces(input_string)
print(result)
