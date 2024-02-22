def generate_squares(N):
    for number in range(1, N + 1):
        yield number ** 2

# Example usage
N = 5
squares_generator = generate_squares(N)

for square in squares_generator:
    print(square)