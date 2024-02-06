def histogram(numbers):
    """
    Prints a histogram to the screen for a given list of integers.

    Parameters:
    - numbers: List of integers.
    """
    for num in numbers:
        # Print '*' for each occurrence of the number
        print('*' * num)

# Example usage:
numbers_list = [4, 9, 7]
histogram(numbers_list)