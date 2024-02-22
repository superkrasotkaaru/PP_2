def generate_divisible_by_3_and_4(n):
    for number in range(0, n + 1):
        if number % 3 == 0 and number % 4 == 0:
            yield number

# Example usage
def main():
    # Get input from the console
    n = int(input("Enter the value of n: "))

    # Generate numbers using the generator
    divisible_numbers_generator = generate_divisible_by_3_and_4(n)

    # Print numbers
    print(f"Numbers divisible by 3 and 4 between 0 and {n}:")
    for number in divisible_numbers_generator:
        print(number)

if __name__ == "__main__":
    main()
