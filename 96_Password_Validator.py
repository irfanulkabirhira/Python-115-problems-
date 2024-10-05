# 94. Password Validator: Write a Python program that takes a password as input and checks if it meets the following criteria: at least 8 characters long, contains both uppercase and lowercase letters, and has at least one digit. If the password is valid, print “Password accepted.” If not, use continue to prompt the user to enter a valid password.

import re

def is_valid_password(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return False
    # Check if password contains both uppercase and lowercase letters
    if not any(c.islower() for c in password) or not any(c.isupper() for c in password):
        return False
    # Check if password contains at least one digit
    if not any(c.isdigit() for c in password):
        return False
    return True

while True:
    password = input("Enter your password: ")
    
    if is_valid_password(password):
        print("Password accepted.")
        break
    else:
        print("Password does not meet the criteria. Please try again.")
        continue
