from functools import reduce

def multiply_list(numbers):
    # Use functools.reduce to multiply all numbers in the list
    result = reduce(lambda x, y: x * y, numbers)
    return result

# Example usage
my_numbers = [2, 3, 4, 5]
result = multiply_list(my_numbers)

print(f"The product of the numbers in the list {my_numbers} is: {result}")
