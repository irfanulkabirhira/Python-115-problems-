# 100. Vowel Counter: Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u) in it. Use a for loop and continue to skip counting non-vowel characters.

def count_vowels(input_string):
    # Define a set of vowels
    vowels = "aeiou"
    vowel_count = 0

    # Loop through each character in the string
    for char in input_string.lower():
        if char in vowels:
            vowel_count += 1  # Increment count if the character is a vowel
        else:
            continue  # Skip non-vowel characters

    return vowel_count

# Take input from the user
user_input = input("Enter a string: ")

# Count the number of vowels
num_vowels = count_vowels(user_input)

# Print the result
print(f"The number of vowels in the string is: {num_vowels}")
