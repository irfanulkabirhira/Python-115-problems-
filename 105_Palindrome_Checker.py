# 103. Palindrome Checker: Write a Python function called is_palindrome that takes a string as input and returns True if it is a palindrome and False otherwise. Test the function with different words.

def is_palindrome(s):
    # Normalize the string: remove spaces, convert to lowercase, and remove non-alphanumeric characters
    normalized_str = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]

# Test the function with different words
test_words = ["racecar", "hello", "A man, a plan, a canal, Panama", "Was it a car or a cat I saw?", "No 'x' in Nixon"]

for word in test_words:
    print(f"'{word}' is a palindrome: {is_palindrome(word)}")
