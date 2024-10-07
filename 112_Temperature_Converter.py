# 110. Temperature Converter: Write a Python function called temperature_converter that takes a temperature value and a string representing the scale (‘C’ for Celsius or ‘F’ for Fahrenheit) as input. The function should convert the temperature from one scale to the other using nested functions and return the converted value.

def temperature_converter(value, scale):
    """
    Function to convert temperature between Celsius and Fahrenheit.

    Parameters:
    value (float): The temperature value to convert.
    scale (str): The scale of the temperature ('C' for Celsius or 'F' for Fahrenheit).

    Returns:
    float: The converted temperature value.
    """
    
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    if scale.upper() == 'C':
        return celsius_to_fahrenheit(value)
    elif scale.upper() == 'F':
        return fahrenheit_to_celsius(value)
    else:
        raise ValueError("Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit.")

# Test the function with different values and scales
print(temperature_converter(100, 'C'))  # Output: 212.0
print(temperature_converter(32, 'F'))   # Output: 0.0
