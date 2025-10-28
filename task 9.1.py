# Problem 9.1: Handle IndexError when accessing grades by index

def get_grade_by_index():
    grades = [85, 90, 78, 92, 88]
    print("Available Grades:", grades)

    try:
        index = int(input("Enter the index number of the grade you want to access: "))
        print(f"Grade at index {index}: {grades[index]}")
    except IndexError:
        print("❌ Error: The index you entered is out of range.")
    except ValueError:
        print("❌ Error: Please enter a valid integer index.")
    finally:
        print("✅ Grade lookup operation completed.\n")

# Run the function
get_grade_by_index()
