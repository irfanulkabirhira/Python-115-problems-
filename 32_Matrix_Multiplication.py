# 32. Matrix Multiplication: Write a Python program using nested loops to multiply two matrices.

# Function to multiply two matrices
def multiply_matrices(A, B):
    # Get the dimensions of A and B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Check if matrices can be multiplied
    if cols_A != rows_B:
        return "Matrix multiplication not possible: number of columns in A must be equal to number of rows in B."
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Input matrices
print("Enter the number of rows and columns for matrix A:")
rows_A = int(input("Rows for A: "))
cols_A = int(input("Columns for A: "))

print("Enter the number of rows and columns for matrix B:")
rows_B = int(input("Rows for B: "))
cols_B = int(input("Columns for B: "))

# Ensure matrices can be multiplied
if cols_A != rows_B:
    print("Matrix multiplication not possible.")
else:
    # Input matrix A
    print("Enter the elements of matrix A:")
    A = []
    for i in range(rows_A):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        A.append(row)
    
    # Input matrix B
    print("Enter the elements of matrix B:")
    B = []
    for i in range(rows_B):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        B.append(row)
    
    # Perform matrix multiplication
    result = multiply_matrices(A, B)
    
    # Print the result
    print("Resultant matrix:")
    for row in result:
        print(' '.join(map(str, row)))
