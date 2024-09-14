# 30. Multiplication Table: Write a Python program using nested loops to print the multiplication table from 1 to 10.

# Printing the multiplication table from 1 to 10
print("Multiplication Table from 1 to 10:")

# Outer loop for the first number
for i in range(1, 11):
    # Inner loop for the second number
    for j in range(1, 11):
        # Printing the product of i and j
        print(f"{i} x {j} = {i * j}", end='\t')
    # New line after each row
    print()
