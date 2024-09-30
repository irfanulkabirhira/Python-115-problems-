# 82. Dictionary Key Removal: Given a dictionary of items and their quantities, write a Python program to remove a specific item from the dictionary based on user input.

# Function to remove an item from the dictionary
def remove_item(dictionary, item_to_remove):
    if item_to_remove in dictionary:
        del dictionary[item_to_remove]
        print(f"Item '{item_to_remove}' has been removed.")
    else:
        print(f"Item '{item_to_remove}' not found in the dictionary.")
    return dictionary

# Taking a dictionary and item to remove as input from the user
print("Enter a dictionary of items and their quantities (e.g., {'apple': 10, 'banana': 5}):")
dict_str = input()
items_dict = eval(dict_str)

print("Enter the name of the item to remove:")
item_to_remove = input()

# Removing the item from the dictionary
updated_dict = remove_item(items_dict, item_to_remove)

# Printing the updated dictionary
print("Updated dictionary:")
print(updated_dict)
