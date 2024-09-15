# 34. List Sum: Write a Python program to find the sum of all elements in a given list of integers.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Calculating the sum of the elements in the list
total_sum = sum(numbers)

# Output the result
print(f"The sum of all elements in the list is: {total_sum}")
