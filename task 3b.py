def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def power(base, exponent):
    return base ** exponent
import math

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, width):
    return length * width
from mypackage.pack1 import mathfunctions
from mypackage.pack2 import areafunctions

# Math operations
print("Addition (5 + 3):", mathfunctions.add(5, 3))
print("Multiplication (4 * 6):", mathfunctions.multiply(4, 6))
print("Power (2 ^ 3):", mathfunctions.power(2, 3))

# Area calculations
print("Area of Circle (r=5):", areafunctions.area_circle(5))
print("Area of Rectangle (5 x 3):", areafunctions.area_rectangle(5, 3)) def add(a, b):
    return a + b

