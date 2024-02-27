import re

def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)
    
    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found.')

# Example usage:
input_string = "Abc Xyz HelloWorld PythonProgramming"

find_sequences(input_string)
