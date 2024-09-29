# 79. Dictionary Length: Write a Python program to calculate and print the number of key-value pairs in a given dictionary.

# Function to calculate and print the number of key-value pairs in a dictionary
def print_dict_length(dictionary):
    length = len(dictionary)
    print(f"The number of key-value pairs in the dictionary is: {length}")

# Taking a dictionary as input from the user
print("Enter a dictionary (e.g., {'Alice': 85, 'Bob': 90}):")
input_str = input()
dictionary = eval(input_str)

# Calculating and printing the number of key-value pairs
print_dict_length(dictionary)
