# 44. Matrix Addition: Write a Python program to add two matrices represented as nested lists.

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    # Adding the matrices
    result = [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]
    return result

# Taking two matrices as input from the user
print("Enter the elements of the first matrix row by row (use spaces to separate elements and enter an empty line to end):")
matrix1 = []
while True:
    row = input().strip()
    if not row:
        break
    matrix1.append([int(x) for x in row.split()])

print("Enter the elements of the second matrix row by row (use spaces to separate elements and enter an empty line to end):")
matrix2 = []
while True:
    row = input().strip()
    if not row:
        break
    matrix2.append([int(x) for x in row.split()])

# Adding the two matrices
try:
    result_matrix = add_matrices(matrix1, matrix2)
    print("The resulting matrix after addition is:")
    for row in result_matrix:
        print(" ".join(map(str, row)))
except ValueError as e:
    print(e)
