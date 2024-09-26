# 71. Set Union: Given two sets A and B, write a Python program to find their union and print all the distinct elements from both sets.

# Function to find the union of two sets
def set_union(set1, set2):
    return set1 | set2

# Taking two sets as input from the user
print("Enter the first set (e.g., {1, 2, 3, 4}):")
input_str1 = input()
set1 = eval(input_str1)

print("Enter the second set (e.g., {3, 4, 5, 6}):")
input_str2 = input()
set2 = eval(input_str2)

# Finding the union of the two sets
union = set_union(set1, set2)

# Output the union
print("The union of the two sets is:")
print(union)
