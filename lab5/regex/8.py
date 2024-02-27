import re

def split_at_uppercase(input_string):
    substrings = re.findall('[A-Z][^A-Z]*', input_string)
    return substrings

# Example usage:
input_string = "SplitThisStringAtUppercaseLetters"
result = split_at_uppercase(input_string)
print(result)
