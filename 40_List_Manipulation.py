# 40. List Manipulation: Given two lists of integers, write a Python program to create a new list that contains elements common to both lists.

# Taking two lists of integers as input from the user
# For simplicity, we assume the input is space-separated strings of numbers
input_list1 = input("Enter the first list of integers separated by spaces: ").split()
input_list2 = input("Enter the second list of integers separated by spaces: ").split()

# Converting the input lists of strings to lists of integers
list1 = [int(x) for x in input_list1]
list2 = [int(x) for x in input_list2]

# Finding the common elements between the two lists
common_elements = [value for value in list1 if value in list2]

# Output the new list containing elements common to both lists
print("The list of common elements is:")
print(common_elements)
