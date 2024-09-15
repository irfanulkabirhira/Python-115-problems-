# 35. List Average: Write a Python program to calculate the average of all elements in a given list of integers.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Calculating the sum of the elements in the list
total_sum = sum(numbers)

# Calculating the number of elements in the list
count = len(numbers)

# Calculating the average
average = total_sum / count if count > 0 else 0

# Output the result
print(f"The average of all elements in the list is: {average:.2f}")
