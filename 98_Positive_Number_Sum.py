# 96. Positive Number Sum: Write a Python program that takes positive numbers as input until a negative number is entered. Then, calculate and print the sum of all positive numbers entered. Use a while loop and break to exit the loop when a negative number is encountered.


# Initialize the sum of positive numbers
total_sum = 0

while True:
    # Take user input
    number = float(input("Enter a positive number (or a negative number to stop): "))
    
    # Check if the number is negative
    if number < 0:
        break  # Exit the loop if a negative number is entered
    
    # Add the positive number to the total sum
    total_sum += number

# Print the total sum of positive numbers
print("Sum of all positive numbers entered:", total_sum)
