# 78. Set Membership Test: Write a Python program that takes an element as input and checks if it exists in a given set. Print “Found” if the element is present and “Not Found” otherwise.

# Function to check if an element is in a set
def check_membership(set_input, element):
    if element in set_input:
        return "Found"
    else:
        return "Not Found"

# Taking a set as input from the user
print("Enter a set (e.g., {1, 2, 3, 4}):")
input_str = input()
set_input = eval(input_str)

# Taking an element as input from the user
print("Enter an element to check (e.g., 3):")
element_str = input()
element = eval(element_str)

# Checking membership and printing the result
result = check_membership(set_input, element)
print(result)
