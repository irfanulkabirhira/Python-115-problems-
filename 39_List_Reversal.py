# 39. List Reversal: Write a Python program to reverse a given list without using any built-in functions.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Reversing the list without using built-in functions
reversed_numbers = []
for num in numbers:
    reversed_numbers.insert(0, num)  # Insert each element at the beginning of the new list

# Output the reversed list
print("The reversed list is:")
print(reversed_numbers)
