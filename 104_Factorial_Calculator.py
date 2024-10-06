# 102. Factorial Calculator: Write a Python function called factorial that takes an integer as input and returns its factorial. Test the function with different values.

def factorial(n):
    # Check if the input is a non-negative integer
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test the function with different values
test_values = [0, 1, 5, 7, 10]

for value in test_values:
    print(f"Factorial of {value} is {factorial(value)}")
