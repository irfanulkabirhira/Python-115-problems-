# 21. Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.

# Taking the value of N as input from the user
N = int(input("Enter a non-negative integer N: "))

# Initializing the factorial result
factorial = 1

# Calculating the factorial using a while loop
while N > 0:
    factorial *= N
    N -= 1

# Output the result
print(f"The factorial is: {factorial}")
