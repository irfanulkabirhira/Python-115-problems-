# 55. Tuple Slicing: Given a tuple, write a Python program to extract a slice of elements from it.

# Function to extract a slice from a tuple
def slice_tuple(t, start, end):
    return t[start:end]

# Taking a tuple and slice indices as input from the user
print("Enter a tuple (e.g., (1, 2, 3, 4, 5)):")
input_str = input()
t = eval(input())

print("Enter the start index for slicing:")
start = int(input())

print("Enter the end index for slicing:")
end = int(input())

# Extracting the slice from the tuple
tuple_slice = slice_tuple(t, start, end)

# Output the sliced tuple
print("The sliced tuple is:")
print(tuple_slice)
