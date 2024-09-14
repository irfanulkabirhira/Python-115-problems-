'''
31. Print Patterns: Write a Python program using nested loops to print the following pattern:

*

**

***

****

*****


'''

# Number of rows for the pattern
rows = 5

# Printing the pattern using nested loops
for i in range(1, rows + 1):
    for j in range(i):
        print('*', end='')
    print()  # Move to the next line after printing stars in the current row
