# 97. Word Palindrome Checker: Write a Python program that takes a word as input and checks if it is a palindrome (reads the same forwards and backward). Use continue to skip checking the word if its length is less than 3 characters.

def is_palindrome(word):
    return word == word[::-1]

# Take user input
word = input("Enter a word to check if it's a palindrome: ")

# Check if the length of the word is less than 3 characters
if len(word) < 3:
    print("Word length is less than 3 characters. Skipping the palindrome check.")
else:
    if is_palindrome(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")
