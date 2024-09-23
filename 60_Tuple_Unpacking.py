# 50. Tuple Unpacking: Given a tuple with three elements (x, y, z), write a Python program to unpack the tuple and assign the values to three variables.

# Function to unpack a tuple into three variables
def unpack_tuple(t):
    x, y, z = t
    return x, y, z

# Taking a tuple with three elements as input from the user
print("Enter a tuple with three elements (e.g., (1, 2, 3)):")
input_str = input()
t = eval(input())

# Unpacking the tuple
x, y, z = unpack_tuple(t)

# Output the unpacked values
print("The values of the unpacked tuple are:")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
