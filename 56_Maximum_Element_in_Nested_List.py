# 66. Maximum Element in Nested List: Write a Python program to find the maximum element in a nested list of integers.

# Function to find the maximum element in a nested list
def find_max_element(nested_list):
    max_element = None
    for sublist in nested_list:
        for item in sublist:
            if isinstance(item, int):
                if max_element is None or item > max_element:
                    max_element = item
    return max_element

# Taking a nested list as input from the user
# For simplicity, we assume the input is a string representing the nested list
print("Enter a nested list (e.g., [[1, 2], [3, 4, 6], [5]]):")
input_str = input()
nested_list = eval(input_str)

# Finding the maximum element
max_element = find_max_element(nested_list)

# Output the maximum element
print("The maximum element in the nested list is:")
print(max_element)
