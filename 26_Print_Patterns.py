# 26. Print Patterns: Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on.

# Function to print a right-angled triangle pattern
def print_right_angled_triangle(n):
    print("Right-angled Triangle:")
    for i in range(1, n + 1):
        print('*' * i)
    print()  # For a new line after the pattern

# Function to print an inverted right-angled triangle pattern
def print_inverted_right_angled_triangle(n):
    print("Inverted Right-angled Triangle:")
    for i in range(n, 0, -1):
        print('*' * i)
    print()  # For a new line after the pattern

# Function to print a pyramid pattern
def print_pyramid(n):
    print("Pyramid:")
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    print()  # For a new line after the pattern

# Function to print an inverted pyramid pattern
def print_inverted_pyramid(n):
    print("Inverted Pyramid:")
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    print()  # For a new line after the pattern

# Taking the number of rows as input from the user
rows = int(input("Enter the number of rows for the patterns: "))

# Print the patterns
print_right_angled_triangle(rows)
print_inverted_right-angled_triangle(rows)
print_pyramid(rows)
print_inverted_pyramid(rows)
