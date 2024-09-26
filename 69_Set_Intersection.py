# 70. Set Intersection: Given two sets A and B, write a Python program to find their intersection and print the common elements.

# Function to find the intersection of two sets
def set_intersection(set1, set2):
    return set1 & set2

# Taking two sets as input from the user
print("Enter the first set (e.g., {1, 2, 3, 4}):")
input_str1 = input()
set1 = eval(input_str1)

print("Enter the second set (e.g., {3, 4, 5, 6}):")
input_str2 = input()
set2 = eval(input_str2)

# Finding the intersection of the two sets
intersection = set_intersection(set1, set2)

# Output the intersection
print("The intersection of the two sets is:")
print(intersection)
