# 19. Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.

# Taking an integer as input from the user
number = int(input("Enter an integer: "))

# Determining the range in which the number falls
if 0 <= number <= 50:
    range_description = "0-50"
elif 51 <= number <= 100:
    range_description = "51-100"
elif 101 <= number <= 150:
    range_description = "101-150"
else:
    range_description = "Above 150"

# Output the range
print(f"The number falls in the range: {range_description}")
