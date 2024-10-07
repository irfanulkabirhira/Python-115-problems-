# 106. Greatest Common Divisor (GCD) Calculator: Write a Python function called gcd that takes two integers as input and returns their greatest common divisor. Test the function with different pairs of numbers.

def gcd(a, b):
    """
    Function to calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The GCD of the two integers.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Test the function with different pairs of numbers
test_pairs = [
    (48, 18),
    (56, 98),
    (101, 10),
    (20, 15),
    (81, 153)
]

for pair in test_pairs:
    print(f"The GCD of {pair[0]} and {pair[1]} is {gcd(pair[0], pair[1])}")
