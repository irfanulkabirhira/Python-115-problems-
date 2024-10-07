# 105. List Sum Calculator: Write a Python function called list_sum that takes a list of integers as input and returns the sum of all elements in the list. Test the function with different lists.


def list_sum(numbers):
    """
    Function to calculate the sum of all elements in a list of integers.
    
    Parameters:
    numbers (list of int): The list of integers to sum.
    
    Returns:
    int: The sum of all elements in the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total

# Test the function with different lists
test_lists = [
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4, -5],
    [10, 20, 30],
    [0, 0, 0],
    [5, 15, 25, 35, 45]
]

for lst in test_lists:
    print(f"The sum of {lst} is {list_sum(lst)}")
