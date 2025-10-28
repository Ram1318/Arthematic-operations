# Task 5.2: Sorting student records by score using Bubble Sort

def bubble_sort_students(students):
    """
    Sorts a list of student dictionaries by their score in ascending order
    using the Bubble Sort algorithm.
    :param students: List of dictionaries with 'name' and 'score' keys
    :return: Sorted list of students
    """
    n = len(students)
    # Traverse through all student records
    for i in range(n - 1):
        # Last i elements are already sorted
        for j in range(n - i - 1):
            if students[j]['score'] > students[j + 1]['score']:
                # Swap the two student dictionaries
                students[j], students[j + 1] = students[j + 1], students[j]
    return students


# --- Example Usage ---

students = [
    {'name': 'Ravi', 'score': 88},
    {'name': 'Priya', 'score': 75},
    {'name': 'Kiran', 'score': 92},
    {'name': 'Anita', 'score': 68}
]

print("Before Sorting (Student Records):")
for s in students:
    print(s)

# Sort using Bubble Sort
bubble_sort_students(students)

print("\nAfter Sorting (Ascending Order by Score):")
for s in students:
    print(s)
