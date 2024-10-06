# 104. Even or Odd Checker: Write a Python function called even_or_odd that takes an integer as input and returns “Even” if the number is even and “Odd” if the number is odd. Test the function with different numbers.


def even_or_odd(num):
    """
    Function to check if a number is even or odd.
    
    Parameters:
    num (int): The integer to check.
    
    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function with different numbers
test_numbers = [0, 1, 2, 3, 10, 15, 20, 21]

for number in test_numbers:
    print(f"{number} is {even_or_odd(number)}")
