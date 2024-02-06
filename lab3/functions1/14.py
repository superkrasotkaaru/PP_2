import math

def sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.

    Parameters:
    - radius: The radius of the sphere.

    Returns:
    - The volume of the sphere.
    """
    volume = (4/3) * math.pi * radius**3
    return volume

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

# Example usage in the same file
if __name__ == "__main__":
    # Testing the sphere_volume function
    radius = float(input("Enter the radius of the sphere: "))
    result_volume = sphere_volume(radius)
    print(f"The volume of the sphere with radius {radius} is: {result_volume:.2f}")

    # Testing the is_palindrome function
    user_input = input("Enter a word or phrase: ")
    result_palindrome = is_palindrome(user_input)

    if result_palindrome:
        print(f"{user_input} is a palindrome.")
    else:
        print(f"{user_input} is not a palindrome.")