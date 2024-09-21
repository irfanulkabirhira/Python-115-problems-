# 63. Matrix Transpose: Write a Python program to transpose a given matrix represented as a nested list.

# Function to transpose a matrix
def transpose_matrix(matrix):
    # Using list comprehension to transpose the matrix
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Taking a matrix as input from the user
# For simplicity, we assume the input is a string representing the matrix
print("Enter a matrix row by row (use spaces to separate elements and enter an empty line to end):")
matrix = []
while True:
    row = input().strip()
    if not row:
        break
    matrix.append([int(x) for x in row.split()])

# Transposing the matrix
transposed = transpose_matrix(matrix)

# Output the transposed matrix
print("The transposed matrix is:")
for row in transposed:
    print(" ".join(map(str, row)))
