# 20. Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.

# Taking the value of N as input from the user
N = int(input("Enter a positive integer N: "))

# Initializing the sum
sum_of_numbers = 0

# Calculating the sum using a for loop
for i in range(1, N + 1):
    sum_of_numbers += i

# Output the result
print(f"The sum of the first {N} natural numbers is: {sum_of_numbers}")
