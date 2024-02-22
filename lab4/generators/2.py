def generate_even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number

# Get input from the console
n = int(input("Enter the value of n: "))

# Generate even numbers using the generator
even_numbers_generator = generate_even_numbers(n)

# Print even numbers in comma-separated form
even_numbers_str = ', '.join(map(str, even_numbers_generator))
print(f"Even numbers between 0 and {n}: {even_numbers_str}")
