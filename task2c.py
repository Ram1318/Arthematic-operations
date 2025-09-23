# Input from user
number = input("Enter a number: ")

# Remove negative sign or decimal point if present
filtered_number = number.replace("-", "").replace(".", "")

# Count digits
digit_count = 0
for char in filtered_number:
    if char.isdigit():
        digit_count += 1

# Output result
print("Total number of digits:", digit_count)
