# 88. Nested Dictionary Length: Write a Python program to calculate and print the total number of key-value pairs in a nested dictionary.

# Sample nested dictionary
nested_dict = {
    'student1': {
        'name': 'Alice',
        'age': 20,
        'address': {
            'street': '123 Maple Street',
            'city': 'Springfield'
        }
    },
    'student2': {
        'name': 'Bob',
        'age': 22,
        'address': {
            'street': '456 Oak Avenue',
            'city': 'Metropolis'
        }
    },
    'student3': {
        'name': 'Charlie',
        'age': 21,
        'address': {
            'street': '789 Pine Road',
            'city': 'Gotham'
        }
    }
}

# Function to calculate the total number of key-value pairs in a nested dictionary
def count_key_value_pairs(d):
    count = 0
    for key, value in d.items():
        count += 1  # Count the current key-value pair
        if isinstance(value, dict):
            count += count_key_value_pairs(value)  # Recursively count key-value pairs in nested dictionaries
    return count

# Calculate and print the total number of key-value pairs
total_pairs = count_key_value_pairs(nested_dict)
print(f"Total number of key-value pairs in the nested dictionary: {total_pairs}")
