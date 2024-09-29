# 77. Dictionary Manipulation: Given a dictionary with student names as keys and their corresponding scores as values, write a Python program to add a new student to the dictionary and update the score of an existing student.

# Function to add a new student and update an existing student's score
def manipulate_dictionary(student_dict, new_student, new_score, existing_student, updated_score):
    # Add new student
    student_dict[new_student] = new_score
    # Update existing student's score
    if existing_student in student_dict:
        student_dict[existing_student] = updated_score
    else:
        print(f"{existing_student} is not in the dictionary.")
    
    return student_dict

# Sample dictionary of student names and scores
student_dict = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

print("Initial dictionary:")
print(student_dict)

# Input for new student
print("Enter the name of the new student:")
new_student = input()

print("Enter the score of the new student:")
new_score = int(input())

# Input for updating existing student's score
print("Enter the name of the student whose score you want to update:")
existing_student = input()

print("Enter the new score for the existing student:")
updated_score = int(input())

# Manipulate the dictionary
updated_dict = manipulate_dictionary(student_dict, new_student, new_score, existing_student, updated_score)

# Output the updated dictionary
print("Updated dictionary:")
print(updated_dict)
