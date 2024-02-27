import re

def replace_characters(input_string):
    pattern = re.compile(r'[ ,.]+')
    result = re.sub(pattern, ':', input_string)
    return result

# Example usage:
input_string = "Hello, world. How are you today?"

result_string = replace_characters(input_string)
print(f'Original string: {input_string}')
print(f'Result string:   {result_string}')
