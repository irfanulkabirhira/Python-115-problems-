# 76. Set Superset Check: Given two sets A and B, write a Python program to check if set A is a superset of set B and print the result.


# Function to check if set A is a superset of set B
def is_superset(setA, setB):
    return setA.issuperset(setB)

# Taking two sets as input from the user
print("Enter the first set A (e.g., {1, 2, 3, 4, 5}):")
input_strA = input()
setA = eval(input_strA)

print("Enter the second set B (e.g., {3, 4}):")
input_strB = input()
setB = eval(input_strB)

# Checking if set A is a superset of set B
result = is_superset(setA, setB)

# Output the result
if result:
    print("Set A is a superset of set B.")
else:
    print("Set A is not a superset of set B.")
