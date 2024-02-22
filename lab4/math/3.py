import math

def regular_polygon_area(n, s):
    cot_angle = math.cos(math.pi / n) / math.sin(math.pi / n)
    area = 0.25 * n * s**2 / cot_angle
    return area

# Get input from the console
n = int(input("Enter the number of sides of the regular polygon: "))
s = float(input("Enter the length of each side: "))

# Calculate the area of the regular polygon
area = regular_polygon_area(n, s)

# Print the result
print(f"The area of the regular polygon is: {area}")
