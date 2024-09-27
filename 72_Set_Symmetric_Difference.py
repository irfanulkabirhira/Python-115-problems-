# 73. Set Symmetric Difference: Given two sets A and B, write a Python program to find the symmetric difference between the two sets (i.e., elements that are present in either set A or set B, but not in both) and print the result.

# Function to find the symmetric difference between two sets
def set_symmetric_difference(set1, set2):
    return set1 ^ set2

# Taking two sets as input from the user
print("Enter the first set (e.g., {1, 2, 3, 4}):")
input_str1 = input()
set1 = eval(input_str1)

print("Enter the second set (e.g., {3, 4, 5, 6}):")
input_str2 = input()
set2 = eval(input_str2)

# Finding the symmetric difference between the two sets
symmetric_difference = set_symmetric_difference(set1, set2)

# Output the symmetric difference
print("The symmetric difference between the two sets is:")
print(symmetric_difference)
