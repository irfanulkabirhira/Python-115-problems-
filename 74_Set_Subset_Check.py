# 75. Set Subset Check: Given two sets A and B, write a Python program to check if set A is a subset of set B and print the result.

# Function to check if set A is a subset of set B
def is_subset(setA, setB):
    return setA.issubset(setB)

# Taking two sets as input from the user
print("Enter the first set A (e.g., {1, 2, 3, 4}):")
input_strA = input()
setA = eval(input_strA)

print("Enter the second set B (e.g., {1, 2, 3, 4, 5, 6}):")
input_strB = input()
setB = eval(input_strB)

# Checking if set A is a subset of set B
result = is_subset(setA, setB)

# Output the result
if result:
    print("Set A is a subset of set B.")
else:
    print("Set A is not a subset of set B.")
