# 22. Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.

# Taking the value of N as input from the user
N = int(input("Enter the number to print the multiplication table: "))

# Printing the multiplication table using a for loop
print(f"Multiplication table for {N}:")
for i in range(1, 11):
    print(f"{N} x {i} = {N * i}")
