# Given three variables: a = ‘100’, b = 25, and c = ‘10.5’, write a Python program to perform the following operations and print the results: – Convert a to an integer and add it to b. – Convert c to a float and subtract it from the result of the first operation. – Convert the final result to a string and concatenate it with the string ” is the answer.”

# Given variables
a = '100'
b = 25
c = '10.5'

# Convert `a` to an integer and add it to `b`
a_int = int(a)
result = a_int + b

# Convert `c` to a float and subtract it from the result
c_float = float(c)
result -= c_float

# Convert the final result to a string and concatenate it with the string " is the answer."
result_str = str(result) + " is the answer."

# Output the result
print(result_str)
