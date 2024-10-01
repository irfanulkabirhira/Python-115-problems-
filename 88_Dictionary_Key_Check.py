# 86. Dictionary Key Check: Write a Python program that takes a key as input and checks if it exists in a given dictionary. Print “Key Found” if the key is present and “Key Not Found” otherwise.


# Function to check if a key exists in the dictionary
def check_key_in_dict(dictionary, key):
    if key in dictionary:
        print("Key Found")
    else:
        print("Key Not Found")

# Taking a dictionary and key as input from the user
print("Enter a dictionary (e.g., {'name': 'Alice', 'age': 30}):")
dict_str = input()
dictionary = eval(dict_str)

print("Enter the key to search for:")
key = input()

# Checking if the key exists in the dictionary
check_key_in_dict(dictionary, key)
