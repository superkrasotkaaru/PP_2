import re

def match_pattern(input_string):
    pattern = re.compile(r'a.*b$')
    match = pattern.match(input_string)
    
    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')

# Example usage:
input_string1 = "acccb"
input_string2 = "abb"
input_string3 = "adefgb"
input_string4 = "abcde"

match_pattern(input_string1)
match_pattern(input_string2)
match_pattern(input_string3)
match_pattern(input_string4)
