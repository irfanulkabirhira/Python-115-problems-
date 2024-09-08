# Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

# Taking a number as input from the user
number = float(input("Enter a number: "))

# Checking if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
