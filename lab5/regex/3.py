import re

def find_sequences(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(input_string)
    
    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found.')

# Example usage:
input_string = "abc_def ghi_jkl mnopq rst_uv wx_yz"

find_sequences(input_string)
