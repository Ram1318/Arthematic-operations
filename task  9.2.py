# Problem 9.2: Handle ZeroDivisionError in a calculator

def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("❌ Error: Division by zero is not allowed.")
    except ValueError:
        print("❌ Error: Please enter valid numeric values.")
    else:
        print(f"✅ Result: {num1} ÷ {num2} = {result}")
    finally:
        print("✅ Division operation completed.\n")

# Run the function
divide_numbers()
