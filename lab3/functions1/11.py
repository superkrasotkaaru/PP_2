def is_palindrome(input_str):
    """
    Checks whether a word or phrase is a palindrome.

    Parameters:
    - input_str: The input word or phrase.

    Returns:
    - True if the input is a palindrome, False otherwise.
    """
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

# Example usage:
user_input = input("Enter a word or phrase: ")
result = is_palindrome(user_input)

if result:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")