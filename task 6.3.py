# Problem 6.3: Write employee details to employee_report.txt

def write_employee_report(employees):
    with open("employee_report.txt", "w") as file:
        file.write("Employee Report\n")
        file.write("---------------------------\n")
        for emp in employees:
            file.write(f"Name: {emp['name']}, Department: {emp['department']}\n")
    print("✅ Employee report written to employee_report.txt")

# Example list of employees
employees = [
    {'name': 'Alice', 'department': 'HR'},
    {'name': 'Bob', 'department': 'Finance'},
    {'name': 'Charlie', 'department': 'IT'},
    {'name': 'Diana', 'department': 'Marketing'}
]

# Run function
write_employee_report(employees)
