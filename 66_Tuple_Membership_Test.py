# 57. Tuple Membership Test: Write a Python program that takes an element as input and checks if it exists in a given tuple.


# Function to check if an element exists in a tuple
def check_element_in_tuple(t, element):
    return element in t

# Taking a tuple and an element as input from the user
print("Enter a tuple (e.g., (1, 2, 3, 4)):")
input_str = input()
t = eval(input_str)

print("Enter the element to check for membership:")
element = eval(input())  # Using eval to handle different data types

# Checking if the element exists in the tuple
exists = check_element_in_tuple(t, element)

# Output the result
if exists:
    print(f"The element {element} exists in the tuple.")
else:
    print(f"The element {element} does not exist in the tuple.")
