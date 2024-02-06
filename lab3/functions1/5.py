from itertools import permutations

def print_permutations(input_string):
    # Generate all permutations of the input string
    permuted_strings = permutations(input_string)

    # Print each permutation
    for permuted_string in permuted_strings:
        print(''.join(permuted_string))

# Example usage:
user_input = input("Enter a string: ")
print("All permutations of the string:")
print_permutations(user_input)