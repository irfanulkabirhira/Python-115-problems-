# 61. Nested List Sorting: Given a nested list containing lists of integers, write a Python program to sort the sublists based on their lengths.


# Function to sort sublists based on their lengths
def sort_sublists_by_length(nested_list):
    return sorted(nested_list, key=len)

# Taking a nested list as input from the user
# For simplicity, we assume the input is a string representing the nested list
print("Enter a nested list (e.g., [[1, 2], [3], [4, 5, 6]]):")
input_str = input()
nested_list = eval(input_str)

# Sorting the sublists by their lengths
sorted_list = sort_sublists_by_length(nested_list)

# Output the sorted list
print("The nested list sorted by sublist lengths is:")
print(sorted_list)
