def solve(numheads, numlegs):
    # Calculate the number of rabbits (r) and chickens (c)
    # where r + c = numheads and 4r + 2c = numlegs
    # Solve the system of equations
    for r in range(numheads + 1):
        c = numheads - r
        if (4 * r + 2 * c) == numlegs:
            return r, c
    # If no solution is found
    return None

# Given number of heads and legs
numheads = 35
numlegs = 94

# Call the solve function and get the result
result = solve(numheads, numlegs)

# Display the result
if result:
    rabbits, chickens = result
    print(f"There are {chickens} chickens and {rabbits} rabbits.")
else:
    print("No solution found.")