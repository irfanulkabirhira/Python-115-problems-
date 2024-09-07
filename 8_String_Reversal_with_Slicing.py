# Write a Python function to reverse a given string using slicing.

def reverse_string_with_slicing(s):
    return s[::-1]

# Example usage
input_string = "OpenAI"
reversed_string = reverse_string_with_slicing(input_string)
print("Reversed string:", reversed_string)
