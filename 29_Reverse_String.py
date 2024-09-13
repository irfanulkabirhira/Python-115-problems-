# 29. Reverse String: Write a Python program using a while loop to reverse a given string.

# Taking a string as input from the user
input_string = input("Enter a string to reverse: ")

# Initializing variables
reversed_string = ""
index = len(input_string) - 1

# Reversing the string using a while loop
while index >= 0:
    reversed_string += input_string[index]
    index -= 1

# Output the reversed string
print("Reversed string:", reversed_string)
