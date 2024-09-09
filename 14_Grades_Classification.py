# 14. Grades Classification: Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

# Taking the student's percentage as input from the user
percentage = float(input("Enter the student's percentage: "))

# Determining the grade based on the percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"

# Output the grade
print(f"The student's grade is: {grade}")
