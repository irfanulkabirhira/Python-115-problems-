# 27. Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

# Taking the value of N as input from the user
N = int(input("Enter a positive integer N: "))

# Handling edge cases
if N <= 1:
    is_prime = False
elif N == 2:
    is_prime = True
else:
    # Initializing the check
    is_prime = True
    divisor = 2
    
    # Checking for factors
    while divisor * divisor <= N:
        if N % divisor == 0:
            is_prime = False
            break
        divisor += 1

# Output the result
if is_prime:
    print(f"{N} is a prime number.")
else:
    print(f"{N} is not a prime number.")
