import time
import math

def delayed_square_root(value):
    # Sleep for 2 seconds (2000 milliseconds)
    time.sleep(2)
    
    # Calculate the square root
    result = math.sqrt(value)
    print(f"The square root of {value} is: {result}")

# Example usage
number_to_square_root = 25
print(f"Delaying the square root calculation for 2 seconds...")
delayed_square_root(number_to_square_root)
