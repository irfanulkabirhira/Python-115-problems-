# 15. Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

# Taking a single character as input from the user
char = input("Enter a single character: ").lower()

# Checking if the input is a single character
if len(char) != 1 or not char.isalpha():
    print("Please enter a single alphabetic character.")
else:
    # Determining if the character is a vowel or consonant
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
