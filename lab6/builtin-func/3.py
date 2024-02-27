def is_palindrome(input_string):
    # Convert the input string to lowercase and remove spaces
    cleaned_string = ''.join(input_string.lower().split())

    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome.")
