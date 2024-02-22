import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Get input from the console
degrees = float(input("Enter the degree value: "))

# Convert degrees to radians
radians = degrees_to_radians(degrees)

# Print the result
print(f"{degrees} degrees is equal to {radians} radians.")
