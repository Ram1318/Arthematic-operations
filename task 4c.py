# Python Program: Demonstrating Dictionary Operations

# 1. Create a Dictionary
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'is_student': False,
    'skills': ['Python', 'Data Analysis', 'Machine Learning']
}
print("1️⃣ Created Dictionary:")
print(person)

# 2. Access Values
print("\n2️⃣ Accessing Values:")
print("Name:", person['name'])
print("Age:", person['age'])
print("City:", person['city'])

# 3. Modify Dictionary
print("\n3️⃣ Modifying Dictionary:")

# Update existing value
person['age'] = 31
print("Updated Age:", person['age'])

# Add new key-value pair
person['country'] = 'USA'
print("Added Country:", person['country'])

# Remove an existing key-value pair
removed_value = person.pop('is_student')
print("Removed 'is_student':", removed_value)

print("Updated Dictionary:")
print(person)

# 4. Iterate Over Dictionary
print("\n4️⃣ Iterating Over Dictionary:")

print("Keys:")
for key in person.keys():
    print(key)

print("\nValues:")
for value in person.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in person.items():
    print(f"{key}: {value}")
