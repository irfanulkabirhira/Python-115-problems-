# 114. Binary Search: Write a recursive Python function called binary_search that takes a sorted list and a target value as input and returns the index of the target value in the list using binary search. If the target value is not in the list, return -1.

def binary_search(sorted_list, target, low, high):
    """
    Recursive function to perform binary search on a sorted list.

    Parameters:
    sorted_list (list): The list to search in (must be sorted).
    target (int): The value to search for.
    low (int): The starting index of the sublist to search in.
    high (int): The ending index of the sublist to search in.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    if low > high:
        return -1  # Target is not in the list

    mid = (low + high) // 2

    if sorted_list[mid] == target:
        return mid  # Target found at index mid
    elif sorted_list[mid] < target:
        # Search in the right half
        return binary_search(sorted_list, target, mid + 1, high)
    else:
        # Search in the left half
        return binary_search(sorted_list, target, low, mid - 1)

# Wrapper function to simplify the call
def find_target(sorted_list, target):
    return binary_search(sorted_list, target, 0, len(sorted_list) - 1)

# Test the function with a sorted list and target values
print(find_target([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))  # Output: 6 (index of 7)
print(find_target([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))  # Output: 1 (index of 2)
print(find_target([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)) # Output: -1 (11 is not in the list)
