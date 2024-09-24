# 52. Tuple Frequency Count: Given a tuple containing various elements, write a Python program to count the frequency of a specific element in the tuple.

# Function to count the frequency of a specific element in a tuple
def count_element_frequency(t, element):
    return t.count(element)

# Taking a tuple and the element to count as input from the user
print("Enter a tuple (e.g., (1, 2, 3, 2, 4, 2)):")
input_str = input()
t = eval(input())

print("Enter the element to count:")
element = eval(input())  # Using eval to handle different data types

# Counting the frequency of the element
frequency = count_element_frequency(t, element)

# Output the frequency
print(f"The element {element} appears {frequency} times in the tuple.")
