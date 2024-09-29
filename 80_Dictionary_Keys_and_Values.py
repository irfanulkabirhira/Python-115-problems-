# 78. Dictionary Keys and Values: Write a Python program that takes a dictionary as input and prints all the keys and values in separate lines.

# Function to print keys and values of a dictionary
def print_keys_and_values(dictionary):
    print("Keys:")
    for key in dictionary.keys():
        print(key)
    
    print("\nValues:")
    for value in dictionary.values():
        print(value)

# Taking a dictionary as input from the user
print("Enter a dictionary (e.g., {'Alice': 85, 'Bob': 90}):")
input_str = input()
dictionary = eval(input_str)

# Printing keys and values
print_keys_and_values(dictionary)
