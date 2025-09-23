# Import custom modules
import add
import subtract
import multiply
import divide

# User input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

# Perform operation
if operation == '+':
    result = add.add(a, b)
elif operation == '-':
    result = subtract.subtract(a, b)
elif operation == '*':
    result = multiply.multiply(a, b)
elif operation == '/':
    result = divide.divide(a, b)
else:
    result = "Invalid operation."

print("Result:", result)
