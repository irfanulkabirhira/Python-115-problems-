# 18. Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.

import cmath

# Taking the coefficients a, b, and c as input from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculating the discriminant
discriminant = b**2 - 4*a*c

# Finding the roots based on the discriminant
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print(f"Root 1: {root1.real:.2f}")
    print(f"Root 2: {root2.real:.2f}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2 * a)
    print(f"Root: {root:.2f}")
else:
    # Complex roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
