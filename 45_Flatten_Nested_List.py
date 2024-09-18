# 45. Flatten Nested List: Write a Python program to flatten a given nested list and convert it into a single-dimensional list.

# Function to flatten a nested list
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            # Recursively flatten the sublist
            flat_list.extend(flatten_list(item))
        else:
            # Add the non-list item to the flat list
            flat_list.append(item)
    return flat_list

# Taking a nested list as input from the user
# For simplicity, we assume the input is a string representing the nested list
input_str = input("Enter a nested list (e.g., [1, [2, 3], [4, [5, 6]]]): ")
nested_list = eval(input_str)

# Flattening the nested list
flat_list = flatten_list(nested_list)

# Output the flattened list
print("The flattened list is:")
print(flat_list)
