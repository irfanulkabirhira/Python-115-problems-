# Write a Python program that takes two strings as input and concatenates them into a single string without using the + operator.

# Taking two strings as input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Concatenating the strings using the `join` method
concatenated_string = "".join([string1, string2])

# Output the result
print("Concatenated string:", concatenated_string)
