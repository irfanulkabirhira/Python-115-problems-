# 108. Math Operations: Write a Python function called math_operations that takes three numbers and a string representing an operation (‘add’, ‘subtract’, ‘multiply’, or ‘divide’). The function should return the result of the specified operation on the three numbers. Implement the math operations as nested functions.

def math_operations(num1, num2, num3, operation):
    """
    Function to perform a specified mathematical operation on three numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    num3 (float): The third number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the specified operation.
    """
    
    def add(a, b, c):
        return a + b + c
    
    def subtract(a, b, c):
        return a - b - c
    
    def multiply(a, b, c):
        return a * b * c
    
    def divide(a, b, c):
        if b == 0 or c == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b / c
    
    # Select the appropriate operation based on the input
    if operation == 'add':
        return add(num1, num2, num3)
    elif operation == 'subtract':
        return subtract(num1, num2, num3)
    elif operation == 'multiply':
        return multiply(num1, num2, num3)
    elif operation == 'divide':
        return divide(num1, num2, num3)
    else:
        raise ValueError("Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'.")

# Test the function with different operations
print(math_operations(10, 5, 2, 'add'))       # Output: 17
print(math_operations(10, 5, 2, 'subtract'))  # Output: 3
print(math_operations(10, 5, 2, 'multiply'))  # Output: 100
print(math_operations(10, 5, 2, 'divide'))    # Output: 1.0
