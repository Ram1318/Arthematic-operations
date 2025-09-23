# Program a: Arithmetic Operations
# Enter two numbers and perform arithmetic operations

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Handling division by zero
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")
