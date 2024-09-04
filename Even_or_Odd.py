# Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd.
# Taking input from the user
number = int(input("Enter an integer: "))

# Checking if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
