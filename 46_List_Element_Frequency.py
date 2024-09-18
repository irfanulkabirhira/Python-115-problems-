# 46. List Element Frequency: Given a nested list containing lists of integers, write a Python program to count the frequency of each element in the entire nested list.

from collections import Counter

# Function to flatten a nested list
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# Function to count the frequency of each element
def count_frequencies(flat_list):
    return Counter(flat_list)

# Taking a nested list as input from the user
# For simplicity, we assume the input is a string representing the nested list
input_str = input("Enter a nested list (e.g., [1, [2, 3], [4, [2, 5]]]): ")
nested_list = eval(input_str)

# Flattening the nested list
flat_list = flatten_list(nested_list)

# Counting the frequency of each element
frequency_count = count_frequencies(flat_list)

# Output the frequency count
print("The frequency of each element is:")
for element, count in frequency_count.items():
    print(f"Element {element}: {count} times")
