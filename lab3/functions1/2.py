def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Input Fahrenheit temperature from the user
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Calculate and display the equivalent Celsius temperature
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")