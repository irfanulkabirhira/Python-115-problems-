# 24. Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.

# Taking the limit N as input from the user
N = int(input("Enter the limit N for the Fibonacci sequence: "))

# Initializing the first two Fibonacci numbers
a, b = 0, 1

# Printing the Fibonacci sequence up to the limit N
print("Fibonacci sequence up to", N, ":")
print(a, end=' ')
for _ in range(1, N):
    a, b = b, a + b
    if a > N:
        break
    print(a, end=' ')
print()  # For a new line after the sequence
