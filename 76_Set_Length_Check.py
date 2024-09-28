# 77. Set Length Check: Write a Python program that takes a set as input and prints the number of elements in the set.

# Function to get the number of elements in a set
def set_length(set_input):
    return len(set_input)

# Taking a set as input from the user
print("Enter a set (e.g., {1, 2, 3, 4}):")
input_str = input()
set_input = eval(input_str)

# Getting the length of the set
length = set_length(set_input)

# Output the number of elements
print("The number of elements in the set is:")
print(length)
