def unique_elements(input_list):
    """
    Returns a new list with unique elements of the input list.

    Parameters:
    - input_list: The input list.

    Returns:
    - A new list with unique elements.
    """
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(original_list)
print(f"Original List: {original_list}")
print(f"Unique Elements: {result}")
