# 95. Divisible by 3 or 5: Write a Python program to print all numbers from 1 to 50 that are divisible by either 3 or 5. Use a for loop and continue to skip numbers that are not divisible by either 3 or 5.

# Print numbers from 1 to 50 that are divisible by either 3 or 5
for number in range(1, 51):
    if number % 3 != 0 and number % 5 != 0:
        continue  # Skip numbers not divisible by 3 or 5
    print(number)
