# Task 5.1: Searching for an employee by ID

def find_employee_by_id(employees, target_id):
    """
    Finds an employee record by their ID.
    :param employees: List of employee dictionaries
    :param target_id: ID to search for
    :return: Employee dictionary if found, else None
    """
    for employee in employees:
        if employee['id'] == target_id:
            return employee  # Return the matching record
    return None  # Return None if not found


# --- Example Usage ---
employees = [
    {'id': 101, 'name': 'Alice', 'department': 'HR'},
    {'id': 102, 'name': 'Bob', 'department': 'Finance'},
    {'id': 103, 'name': 'Charlie', 'department': 'IT'},
    {'id': 104, 'name': 'Diana', 'department': 'Marketing'}
]

# Input: Employee ID to search
target_id = int(input("Enter Employee ID to search: "))

# Function call
result = find_employee_by_id(employees, target_id)

# Display result
if result:
    print("✅ Employee found:")
    print(result)
else:
    print("❌ No employee found with that ID.")
