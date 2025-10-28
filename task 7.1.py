# Problem 7.1: Analyze and manipulate student grades using built-in functions

def analyze_grades(grades):
    print("📘 Student Grades Analysis\n")

    # Display the list and its type
    print("Grades List:", grades)
    print("Type of grades:", type(grades))

    # Length of list
    print("Total number of students:", len(grades))

    # Highest and Lowest scores
    print("Highest Grade:", max(grades))
    print("Lowest Grade:", min(grades))

    # Sorted list (ascending)
    print("Grades in Ascending Order:", sorted(grades))

    # Sorted list (descending)
    print("Grades in Descending Order:", sorted(grades, reverse=True))

    # Reversed list (original order reversed)
    print("Grades in Reverse Order:", list(reversed(grades)))

    # Display index and grade using range()
    print("\nDisplaying Grades with Index:")
    for i in range(len(grades)):
        print(f"Student {i+1}: {grades[i]}")


# --- Example Usage ---
