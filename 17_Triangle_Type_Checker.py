# 17. Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.

# Taking the three sides of the triangle as input from the user
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

# Checking if the sides form a valid triangle
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    # Determining the type of triangle
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
else:
    triangle_type = "Invalid triangle"

# Output the type of triangle
print(f"The triangle is {triangle_type}.")
