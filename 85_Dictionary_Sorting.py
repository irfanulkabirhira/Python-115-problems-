# 83. Dictionary Sorting: Given a dictionary with names as keys and corresponding ages as values, write a Python program to sort the dictionary based on age in ascending order.

# Function to sort a dictionary by its values
def sort_dict_by_values(dictionary):
    # Sorting the dictionary by values (ages) in ascending order
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict

# Taking a dictionary of names and ages as input from the user
print("Enter a dictionary with names as keys and ages as values (e.g., {'Alice': 30, 'Bob': 25}):")
dict_str = input()
names_ages_dict = eval(dict_str)

# Sorting the dictionary by age
sorted_dict = sort_dict_by_values(names_ages_dict)

# Printing the sorted dictionary
print("Dictionary sorted by age in ascending order:")
print(sorted_dict)
