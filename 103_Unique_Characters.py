# 101. Unique Characters: Write a Python program that takes a string as input and checks if it contains all unique characters (no character repeats). Use a for loop and break when a character repeats.


def has_unique_characters(input_string):
    seen_chars = set()  # Use a set to track characters we've encountered

    # Loop through each character in the string
    for char in input_string:
        if char in seen_chars:
            return False  # If the character is already in the set, not unique
        seen_chars.add(char)  # Add the character to the set
    
    return True  # All characters are unique if we get through the loop without finding duplicates

# Take input from the user
user_input = input("Enter a string: ")

# Check if the string has all unique characters
if has_unique_characters(user_input):
    print("The string contains all unique characters.")
else:
    print("The string does not contain all unique characters.")
