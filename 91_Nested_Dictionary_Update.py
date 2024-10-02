# 89. Nested Dictionary Update: Given a nested dictionary of employee details, write a Python program to update an employee’s salary based on their employee ID.

# Sample nested dictionary containing employee details
employees = {
    'emp1': {
        'name': 'Alice',
        'age': 30,
        'salary': 50000,
        'department': 'HR'
    },
    'emp2': {
        'name': 'Bob',
        'age': 35,
        'salary': 60000,
        'department': 'Finance'
    },
    'emp3': {
        'name': 'Charlie',
        'age': 40,
        'salary': 70000,
        'department': 'Engineering'
    }
}

# Function to update an employee's salary based on their employee ID
def update_salary(employee_id, new_salary):
    if employee_id in employees:
        employees[employee_id]['salary'] = new_salary
        print(f"Salary for employee ID '{employee_id}' has been updated to {new_salary}.")
    else:
        print("Employee ID not found.")

# Taking employee ID and new salary as input from the user
print("Enter the employee ID to update the salary (e.g., 'emp1', 'emp2', 'emp3'):")
employee_id = input()
print("Enter the new salary:")
new_salary = float(input())

# Updating the employee's salary
update_salary(employee_id, new_salary)
