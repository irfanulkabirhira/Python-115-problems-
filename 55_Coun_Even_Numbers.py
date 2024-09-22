# 65. Count Even Numbers: Write a Python program to count the number of even numbers in a nested list.

# Function to count the number of even numbers in a nested list
def count_even_numbers(nested_list):
    count = 0
    for sublist in nested_list:
        for item in sublist:
            if isinstance(item, int) and item % 2 == 0:
                count += 1
    return count

# Taking a nested list as input from the user
# For simplicity, we assume the input is a string representing the nested list
print("Enter a nested list (e.g., [[1, 2], [3, 4, 6], [5]]):")
input_str = input()
nested_list = eval(input_str)

# Counting the even numbers
even_count = count_even_numbers(nested_list)

# Output the count of even numbers
print("The number of even numbers in the nested list is:")
print(even_count)
