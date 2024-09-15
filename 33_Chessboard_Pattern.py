# 33. Chessboard Pattern: Write a Python program using nested loops to print a chessboard pattern (alternating “X” and “O” characters) of size 8×8.34. Number Pyramid: Write a Python program using nested loops to print a number pyramid like the following: 1 22 333 4444 55555

# Size of the chessboard
size = 8

# Printing the chessboard pattern
for i in range(size):
    for j in range(size):
        # Print 'X' if the sum of the row and column indices is even, 'O' if odd
        if (i + j) % 2 == 0:
            print('X', end=' ')
        else:
            print('O', end=' ')
    print()  # Move to the next line after each row


    print()


# Number of levels for the pyramid
levels = 5

# Printing the number pyramid
for i in range(1, levels + 1):
    # Print leading spaces for alignment
    print(' ' * (levels - i), end='')
    # Print numbers
    for j in range(i):
        print(i, end='')
    print()  # Move to the next line after each row
