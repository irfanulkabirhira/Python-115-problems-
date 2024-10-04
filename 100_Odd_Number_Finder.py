# 98. Odd Number Finder: Write a Python program to find the first odd number from a list of integers. Use a for loop and break to stop the loop when the first odd number is found.

def find_first_odd(numbers):
    for number in numbers:
        if number % 2 != 0:
            return number  # Return the first odd number found
    return None  # Return None if no odd number is found

# List of integers
numbers = [2, 4, 6, 8, 10, 13, 18]

# Find the first odd number
first_odd = find_first_odd(numbers)

if first_odd is not None:
    print("The first odd number in the list is:", first_odd)
else:
    print("No odd number found in the list.")
