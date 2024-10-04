# 92. Prime Number Checker: Write a Python program that takes a number as input and determines if it is a prime number or not. Use a for loop to check for factors. If a factor is found, break out of the loop.

# Function to check if a number is prime
def is_prime(number):
    # Check if the number is less than 2
    if number <= 1:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, so it's not a prime number
    return True  # No factors found, so it is a prime number

# Taking input from the user
try:
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter an integer.")
