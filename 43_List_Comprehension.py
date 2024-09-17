# 43. List Comprehension: Given a list of integers, write a Python program to create a new list that contains the squares of the elements using list comprehension.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Creating a new list that contains the squares of the elements using list comprehension
squares = [num ** 2 for num in numbers]

# Output the new list with squares
print("The list of squares of the elements is:")
print(squares)
