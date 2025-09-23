# Step 1: Create a tuple
my_tuple = (10, 'hello', 3.14, 'world')
print("Original tuple:", my_tuple)

# Step 2: Access elements and slices
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slice (1:3):", my_tuple[1:3])

# Step 3: Concatenate tuples
tuple2 = (100, 200)
new_tuple = my_tuple + tuple2
print("Concatenated tuple:", new_tuple)

# Step 4: Attempt to modify (should raise an error)
try:
    my_tuple[0] = 99
except TypeError as e:
    print("Error (tuples are immutable):", e)
