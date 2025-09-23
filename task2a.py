# Input from user
score = float(input("Enter the student's score: "))

# Determine grade using conditional statements
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Output result
print("The student's grade is:", grade)

