def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter with a lambda function to filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# Display the result
print("Original list:", numbers)
print("Prime numbers:", prime_numbers)