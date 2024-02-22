def trapezoid_area(a, b, h):
    area = 0.5 * (a + b) * h
    return area

# Get input from the console
a = float(input("Enter the length of the first base (a): "))
b = float(input("Enter the length of the second base (b): "))
h = float(input("Enter the height (h): "))

# Calculate the area of the trapezoid
area = trapezoid_area(a, b, h)

# Print the result
print(f"The area of the trapezoid is: {area}")
