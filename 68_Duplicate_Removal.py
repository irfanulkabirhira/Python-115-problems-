# 69. Duplicate Removal: Write a Python program that takes a list of elements as input and creates a new set containing only the unique elements from the list.

# Function to remove duplicates by converting a list to a set
def remove_duplicates(lst):
    return set(lst)

# Taking a list of elements as input from the user
print("Enter a list of elements (e.g., [1, 2, 2, 3, 4]):")
input_str = input()

# Convert the input string to a list using eval
lst = eval(input_str)

# Removing duplicates and creating a set
unique_set = remove_duplicates(lst)

# Output the unique set
print("The set with unique elements is:")
print(unique_set)
