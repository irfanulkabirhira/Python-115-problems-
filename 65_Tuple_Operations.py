# 56. Tuple Operations: Given two tuples of integers, write a Python program to perform element-wise addition, subtraction, and multiplication and create new tuples for each operation.

# Function to perform element-wise addition, subtraction, and multiplication
def tuple_operations(t1, t2):
    # Ensure both tuples have the same length
    if len(t1) != len(t2):
        raise ValueError("Tuples must be of the same length")
    
    # Element-wise addition
    addition = tuple(a + b for a, b in zip(t1, t2))
    
    # Element-wise subtraction
    subtraction = tuple(a - b for a, b in zip(t1, t2))
    
    # Element-wise multiplication
    multiplication = tuple(a * b for a, b in zip(t1, t2))
    
    return addition, subtraction, multiplication

# Taking two tuples as input from the user
print("Enter the first tuple (e.g., (1, 2, 3)):")
input_str1 = input()
t1 = eval(input_str1)

print("Enter the second tuple (e.g., (4, 5, 6)):")
input_str2 = input()
t2 = eval(input_str2)

# Perform tuple operations
try:
    addition, subtraction, multiplication = tuple_operations(t1, t2)
    
    # Output the results
    print("Element-wise addition:")
    print(addition)
    
    print("Element-wise subtraction:")
    print(subtraction)
    
    print("Element-wise multiplication:")
    print(multiplication)
except ValueError as e:
    print(e)
