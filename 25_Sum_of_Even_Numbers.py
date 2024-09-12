# 25. Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.

# Taking the value of N as input from the user
N = int(input("Enter the value of N: "))

# Initializing variables
sum_even = 0
current = 2  # Start from the first even number

# Calculating the sum of even numbers using a while loop
while current <= N:
    sum_even += current
    current += 2  # Move to the next even number

# Output the result
print(f"The sum of all even numbers between 1 and {N} is: {sum_even}")
