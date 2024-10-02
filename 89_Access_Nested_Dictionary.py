# 87. Access Nested Dictionary: Given a nested dictionary containing student details, write a Python program to access and print specific information such as a student’s name, age, and address.

# Sample nested dictionary containing student details
students = {
    'student1': {
        'name': 'Alice',
        'age': 20,
        'address': '123 Maple Street'
    },
    'student2': {
        'name': 'Bob',
        'age': 22,
        'address': '456 Oak Avenue'
    },
    'student3': {
        'name': 'Charlie',
        'age': 21,
        'address': '789 Pine Road'
    }
}

# Function to access and print student details
def print_student_details(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Address: {student['address']}")
    else:
        print("Student ID not found.")

# Taking student ID as input from the user
print("Enter the student ID (e.g., 'student1', 'student2', 'student3'):")
student_id = input()

# Accessing and printing student details
print_student_details(student_id)
