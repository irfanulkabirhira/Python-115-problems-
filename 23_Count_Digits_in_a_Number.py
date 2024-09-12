# 23. Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.

# Taking the value of N as input from the user
N = int(input("Enter an integer: "))

# Initialize the digit count
digit_count = 0

# Handle the case where N is zero
if N == 0:
    digit_count = 1
else:
    # Using a while loop to count the digits
    temp = abs(N)  # Use the absolute value to handle negative numbers
    while temp > 0:
        digit_count += 1
        temp //= 10

# Output the result
print(f"The number of digits in {N} is: {digit_count}")
