# 81. Dictionary Merging: Given two dictionaries, write a Python program to merge them into a single dictionary and print the result.

# Function to merge two dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of the first dictionary
    merged_dict.update(dict2)   # Update with the second dictionary
    return merged_dict

# Taking two dictionaries as input from the user
print("Enter the first dictionary (e.g., {'a': 1, 'b': 2}):")
dict1_str = input()
dict1 = eval(dict1_str)

print("Enter the second dictionary (e.g., {'c': 3, 'd': 4}):")
dict2_str = input()
dict2 = eval(dict2_str)

# Merging the dictionaries
merged_dict = merge_dictionaries(dict1, dict2)

# Printing the result
print("Merged dictionary:")
print(merged_dict)
