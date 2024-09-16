# 36. List Max and Min: Write a Python program to find the maximum and minimum values in a given list of integers.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Finding the maximum and minimum values in the list
max_value = max(numbers) if numbers else None
min_value = min(numbers) if numbers else None

# Output the results
if numbers:
    print(f"The maximum value in the list is: {max_value}")
    print(f"The minimum value in the list is: {min_value}")
else:
    print("The list is empty. Cannot determine maximum and minimum values.")
