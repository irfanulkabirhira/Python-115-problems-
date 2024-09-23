# 49. Tuple Concatenation: Write a Python program to concatenate two tuples and create a new tuple.

# Function to concatenate two tuples
def concatenate_tuples(tuple1, tuple2):
    return tuple1 + tuple2

# Taking two tuples as input from the user
print("Enter the first tuple (e.g., (1, 2, 3)):")
tuple1 = eval(input())

print("Enter the second tuple (e.g., (4, 5, 6)):")
tuple2 = eval(input())

# Concatenating the tuples
result_tuple = concatenate_tuples(tuple1, tuple2)

# Output the resulting concatenated tuple
print("The concatenated tuple is:")
print(result_tuple)
