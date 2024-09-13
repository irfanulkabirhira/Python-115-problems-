# 28. List Manipulation: Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.

# Taking a list of integers as input from the user
# For simplicity, we are assuming the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Initializing variables for sum, maximum, and minimum values
total_sum = 0
maximum = numbers[0]
minimum = numbers[0]

# Calculating sum, maximum, and minimum using a for loop
for num in numbers:
    total_sum += num
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

# Calculating the average
average = total_sum / len(numbers) if numbers else 0

# Output the results
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
