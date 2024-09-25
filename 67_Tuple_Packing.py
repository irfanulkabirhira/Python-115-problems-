# 58. Tuple Packing: Write a Python program to pack three variables into a single tuple and print the tuple.

# Function to pack three variables into a tuple
def pack_into_tuple(var1, var2, var3):
    return (var1, var2, var3)

# Taking three variables as input from the user
print("Enter the first variable:")
var1 = input()

print("Enter the second variable:")
var2 = input()

print("Enter the third variable:")
var3 = input()

# Packing the variables into a tuple
packed_tuple = pack_into_tuple(var1, var2, var3)

# Output the packed tuple
print("The packed tuple is:")
print(packed_tuple)
