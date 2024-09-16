# 38. List Filtering: Given a list of integers, write a Python program to create a new list that contains only the even numbers from the original list.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Filtering out the even numbers from the list
even_numbers = [num for num in numbers if num % 2 == 0]

# Output the new list containing only even numbers
print("The list of even numbers is:")
print(even_numbers)
