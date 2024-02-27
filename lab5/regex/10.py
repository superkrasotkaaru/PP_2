def camel_to_snake(camel_case_string):
    result = ''.join(['_' + i.lower() if i.isupper() else i for i in camel_case_string]).lstrip('_')
    return result

# Example usage:
camel_case_input = "convertThisCamelCaseString"
snake_case_output = camel_to_snake(camel_case_input)

print(f'Camel Case: {camel_case_input}')
print(f'Snake Case: {snake_case_output}')
