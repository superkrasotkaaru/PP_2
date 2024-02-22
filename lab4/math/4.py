def parallelogram_area(base, height):
    area = base * height
    return area

# Get input from the console
base = float(input("Enter the length of the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

# Calculate the area of the parallelogram
area = parallelogram_area(base, height)

# Print the result
print(f"The area of the parallelogram is: {area}")
