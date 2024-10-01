# 85. Dictionary Comprehension: Given a list of integers, write a Python program to create a dictionary where the keys are the elements from the list, and the values are their squares.

# Function to create a dictionary with keys as elements and values as their squares
def create_square_dict(numbers):
    # Dictionary comprehension to create the dictionary
    square_dict = {num: num**2 for num in numbers}
    return square_dict

# Taking a list of integers as input from the user
print("Enter a list of integers separated by spaces (e.g., 1 2 3 4):")
input_list = input()
numbers = list(map(int, input_list.split()))

# Creating the dictionary with squares
square_dict = create_square_dict(numbers)

# Printing the dictionary
print("Dictionary with elements and their squares:")
print(square_dict)
