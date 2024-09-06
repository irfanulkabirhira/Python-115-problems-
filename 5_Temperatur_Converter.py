# Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.
# Taking Celsius temperature as input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Output the result
print(f"{celsius}°C is equal to {fahrenheit}°F")
