# 59. Nested List Element Access: Given a nested list, write a Python program to access and print specific elements from it.

# Function to access and print specific elements from a nested list
def access_elements(nested_list, indices):
    element = nested_list
    try:
        # Navigate through the nested list using the provided indices
        for index in indices:
            element = element[index]
        print("The accessed element is:", element)
    except (IndexError, TypeError) as e:
        print("Error:", e)

# Taking a nested list as input from the user
print("Enter a nested list (e.g., [[1, 2], [3, [4, 5]]]):")
input_str = input()
nested_list = eval(input_str)

# Taking indices to access specific elements from the nested list
print("Enter indices to access the element (e.g., 0, 1 for the element at [0][1]):")
indices = list(map(int, input().split(',')))

# Accessing and printing the specific element
access_elements(nested_list, indices)
