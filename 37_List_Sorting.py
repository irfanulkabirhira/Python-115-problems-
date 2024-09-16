# 37. List Sorting: Write a Python program to sort a list of integers in ascending order.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Sorting the list in ascending order
numbers.sort()

# Output the sorted list
print("The sorted list in ascending order is:")
print(numbers)


print ()

# Sorting the list in ascending order and creating a new sorted list
sorted_numbers = sorted(numbers)

# Output the sorted list
print("The sorted list in ascending order is:")
print(sorted_numbers)
