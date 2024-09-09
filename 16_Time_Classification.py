# 16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

# Taking the time in hours as input from the user
hours = int(input("Enter the time in hours (24-hour format): "))

# Determining the greeting based on the time
if 0 <= hours < 12:
    greeting = "Good Morning"
elif 12 <= hours < 17:
    greeting = "Good Afternoon"
elif 17 <= hours < 20:
    greeting = "Good Evening"
elif 20 <= hours < 24:
    greeting = "Good Night"
else:
    greeting = "Invalid time. Please enter a time between 0 and 23."

# Output the greeting
print(greeting)
