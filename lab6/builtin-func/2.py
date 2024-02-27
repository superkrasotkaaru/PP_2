def count_upper_lower(string):
    # Initialize counters for upper and lower case letters
    upper_count = 0
    lower_count = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is upper case
        if char.isupper():
            upper_count += 1
        # Check if the character is lower case
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage
input_string = "Hello World"
upper_count, lower_count = count_upper_lower(input_string)

print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")
