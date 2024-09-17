# 42. List Duplicates Removal: Write a Python program to remove duplicates from a given list while preserving the order of the elements.

# Taking a list of integers as input from the user
# For simplicity, we assume the input is a space-separated string of numbers
input_list = input("Enter a list of integers separated by spaces: ").split()

# Converting the input list of strings to a list of integers
numbers = [int(x) for x in input_list]

# Removing duplicates while preserving order
seen = set()
unique_numbers = []
for num in numbers:
    if num not in seen:
        unique_numbers.append(num)
        seen.add(num)

# Output the list with duplicates removed
print("The list with duplicates removed is:")
print(unique_numbers)
