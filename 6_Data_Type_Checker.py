# Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

def check_data_type(variable):
    return type(variable).__name__

# Example usage
var1 = 42
var2 = 3.14
var3 = "Hello"
var4 = [1, 2, 3]

print("Data type of var1:", check_data_type(var1))  # int
print("Data type of var2:", check_data_type(var2))  # float
print("Data type of var3:", check_data_type(var3))  # str
print("Data type of var4:", check_data_type(var4))  # list
