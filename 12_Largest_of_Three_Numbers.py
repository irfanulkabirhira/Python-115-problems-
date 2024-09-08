# Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.

# Taking three numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number
largest = num1  # Assume num1 is the largest initially

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

# Output the largest number
print("The largest number is:", largest)
