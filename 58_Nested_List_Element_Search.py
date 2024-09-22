# 68. Nested List Element Search: Write a Python program to search for a specific element in a nested list and return its position (row and column indices).

# Function to search for an element in a nested list and return its position
def search_element(nested_list, target):
    for row_index, sublist in enumerate(nested_list):
        if target in sublist:
            column_index = sublist.index(target)
            return (row_index, column_index)
    return None

# Taking a nested list and the target element as input from the user
print("Enter a nested list (e.g., [[1, 2], [3, 4, 5], [6]]):")
input_str = input()
nested_list = eval(input_str)

print("Enter the element to search for:")
target = int(input())

# Searching for the element
position = search_element(nested_list, target)

# Output the position of the element
if position:
    print(f"The element {target} is located at position: (row {position[0]}, column {position[1]})")
else:
    print(f"The element {target} was not found in the nested list.")
