def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string

# Example usage:
snake_case_input = "hello_world_how_are_you"
camel_case_output = snake_to_camel(snake_case_input)

print(f'Snake Case: {snake_case_input}')
print(f'Camel Case: {camel_case_output}')
