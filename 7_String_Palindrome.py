# Write a Python function to check if a given string is a palindrome or not.

def is_palindrome(s):
    # Converting the string to lowercase to make the check case-insensitive
    s = s.lower()
    # Removing any spaces from the string
    s = s.replace(" ", "")
    # Checking if the string is equal to its reverse
    return s == s[::-1]

# Example usage
input_string = "Madam"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
