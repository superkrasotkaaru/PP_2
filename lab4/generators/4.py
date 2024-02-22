def squares(a, b):
    for number in range(a, b + 1):
        yield number ** 2

# Test the generator with a for loop
a = 3
b = 7

print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)
