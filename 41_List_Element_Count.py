# 41. List Element Count: Write a Python program to count the occurrences of a specific element in a given list.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Taking the element to count as input from the user
element = int(input("Enter the element to count its occurrences: "))

# Counting the occurrences of the specified element
count = numbers.count(element)

# Output the result
print(f"The element {element} occurs {count} times in the list.")
