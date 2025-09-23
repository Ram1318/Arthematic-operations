# Step 1: Create and add elements
numbers = [10, 5, 8]
print("Initial list:", numbers)

# Add elements
numbers.append(12)
numbers.extend([20, 3])
print("After adding elements:", numbers)

# Step 2: Remove specific element
numbers.remove(5)  # Removes the first occurrence of 5
print("After removing 5:", numbers)

# Step 3: Sort elements
numbers.sort()
print("Sorted (ascending):", numbers)

numbers.sort(reverse=True)
print("Sorted (descending):", numbers)

# Step 4: Find min and max
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

# Step 5: Calculate sum and average
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)
