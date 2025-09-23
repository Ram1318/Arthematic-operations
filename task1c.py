# Program c: Logical Operations
# Enter three numbers and perform logical operations

# Input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

# Logical operations
print("a > b and b > c:", a > b and b > c)
print("a > b or b > c:", a > b or b > c)
print("not (a > b):", not (a > b))
