# 51. Tuple Sorting: Write a Python program to sort a tuple of integers in ascending order.

# Function to sort a tuple of integers in ascending order
def sort_tuple(t):
    # Convert tuple to list, sort the list, and then convert it back to tuple
    sorted_list = sorted(t)
    return tuple(sorted_list)

# Taking a tuple of integers as input from the user
print("Enter a tuple of integers (e.g., (3, 1, 4, 1, 5)):")
input_str = input()
t = eval(input())

# Sorting the tuple
sorted_tuple = sort_tuple(t)

# Output the sorted tuple
print("The sorted tuple is:")
print(sorted_tuple)
