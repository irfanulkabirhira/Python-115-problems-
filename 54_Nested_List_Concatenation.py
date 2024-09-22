# 64. Nested List Concatenation: Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat list.

# Function to concatenate all sublists into a single flat list
def concatenate_sublists(nested_list):
    flat_list = []
    for sublist in nested_list:
        flat_list.extend(sublist)
    return flat_list

# Taking a list of nested lists as input from the user
# For simplicity, we assume the input is a string representing the list of nested lists
print("Enter a list of nested lists (e.g., [[1, 2], [3, 4], [5]]):")
input_str = input()
nested_list = eval(input_str)

# Concatenating the sublists
flat_list = concatenate_sublists(nested_list)

# Output the flat list
print("The concatenated flat list is:")
print(flat_list)
