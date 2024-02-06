def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    """Filter prime numbers from the given list."""
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_primes = filter_prime(numbers_list)
print(f"Original list: {numbers_list}")
print(f"Prime numbers: {filtered_primes}")