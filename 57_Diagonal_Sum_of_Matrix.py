# 67. Diagonal Sum of Matrix: Given a square matrix represented as a nested list, write a Python program to calculate the sum of the elements in the main diagonal.

# Function to calculate the sum of the main diagonal elements of a square matrix
def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]
    return total

# Taking a square matrix as input from the user
# For simplicity, we assume the input is a string representing the matrix
print("Enter a square matrix row by row (use spaces to separate elements and enter an empty line to end):")
matrix = []
while True:
    row = input().strip()
    if not row:
        break
    matrix.append([int(x) for x in row.split()])

# Calculating the sum of the main diagonal
sum_diagonal = diagonal_sum(matrix)

# Output the sum of the main diagonal
print("The sum of the elements in the main diagonal is:")
print(sum_diagonal)
