# 115. Power Calculation: Write a recursive Python function called power that takes two positive integers, base and exponent, as input and returns the value of base raised to the exponent.


def power(base, exponent):
    """
    Recursive function to calculate the power of a base raised to an exponent.

    Parameters:
    base (int): The base value.
    exponent (int): The exponent value.

    Returns:
    int: The result of base raised to the exponent.
    """
    # Base case: exponent is 0
    if exponent == 0:
        return 1
    # Recursive case
    return base * power(base, exponent - 1)

# Test the function with different base and exponent values
print(power(2, 3))  # Output: 8 (2^3)
print(power(5, 4))  # Output: 625 (5^4)
print(power(7, 2))  # Output: 49 (7^2)
