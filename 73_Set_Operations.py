# 74. Set Operations: Given three sets A, B, and C, write a Python program to find and print the intersection of A and B, the union of B and C, and the difference between C and A.

# Function to perform set operations
def set_operations(setA, setB, setC):
    intersection_AB = setA & setB
    union_BC = setB | setC
    difference_CA = setC - setA
    
    return intersection_AB, union_BC, difference_CA

# Taking three sets as input from the user
print("Enter the first set A (e.g., {1, 2, 3, 4}):")
input_strA = input()
setA = eval(input_strA)

print("Enter the second set B (e.g., {3, 4, 5, 6}):")
input_strB = input()
setB = eval(input_strB)

print("Enter the third set C (e.g., {5, 6, 7, 8}):")
input_strC = input()
setC = eval(input_strC)

# Performing set operations
intersection_AB, union_BC, difference_CA = set_operations(setA, setB, setC)

# Output the results
print("The intersection of set A and set B is:")
print(intersection_AB)

print("The union of set B and set C is:")
print(union_BC)

print("The difference between set C and set A is:")
print(difference_CA)
