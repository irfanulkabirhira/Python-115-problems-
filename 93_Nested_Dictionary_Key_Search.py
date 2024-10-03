# 91. Nested Dictionary Key Search: Write a Python program that takes a key as input and searches for it in a nested dictionary. If found, print the corresponding value, otherwise, print “Key Not Found.”


# Sample nested dictionary
nested_dict = {
    'category1': {
        'item1': {
            'name': 'Laptop',
            'price': 1200,
            'quantity': 10
        },
        'item2': {
            'name': 'Smartphone',
            'price': 800,
            'quantity': 25
        }
    },
    'category2': {
        'item3': {
            'name': 'Tablet',
            'price': 300,
            'quantity': 15
        },
        'item4': {
            'name': 'Headphones',
            'price': 150,
            'quantity': 40
        }
    }
}

# Function to search for a key in the nested dictionary
def search_key_in_nested_dict(d, search_key):
    # Recursive function to search for the key
    for key, value in d.items():
        if key == search_key:
            return value
        elif isinstance(value, dict):
            found = search_key_in_nested_dict(value, search_key)
            if found is not None:
                return found
    return None

# Taking key as input from the user
search_key = input("Enter the key to search in the nested dictionary: ")

# Searching for the key
result = search_key_in_nested_dict(nested_dict, search_key)

# Printing the result
if result:
    print(f"Value for the key '{search_key}': {result}")
else:
    print("Key Not Found")
