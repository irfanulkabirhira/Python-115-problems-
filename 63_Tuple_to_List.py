# 53. Tuple to List: Write a Python program to convert a tuple into a list.

# Function to convert a tuple to a list
def tuple_to_list(t):
    return list(t)

# Taking a tuple as input from the user
print("Enter a tuple (e.g., (1, 2, 3, 4)):")
input_str = input()
t = eval(input())

# Converting the tuple to a list
list_from_tuple = tuple_to_list(t)

# Output the converted list
print("The converted list is:")
print(list_from_tuple)
