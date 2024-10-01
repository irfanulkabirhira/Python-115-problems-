# 84. Dictionary Frequency Count: Write a Python program that takes a string as input and creates a dictionary containing each character as a key and its frequency as the value.

# Function to count the frequency of each character in a string
def count_char_frequencies(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

# Taking a string as input from the user
print("Enter a string:")
input_string = input()

# Counting the frequency of each character
frequency_dict = count_char_frequencies(input_string)

# Printing the frequency dictionary
print("Character frequencies:")
print(frequency_dict)
