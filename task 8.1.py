# Problem 8.1: Generator Function for Number Sequence

def number_sequence(start=0, end=10, step=1):
    """
    Generator that produces a sequence of numbers from start to end with the given step.
    Default: 0 to 10 with step 1
    """
    current = start
    while current <= end:
        yield current
        current += step


# --- Example Usage ---

print("📘 Sequence with Custom Range (Start=5, End=20, Step=5):")
for num in number_sequence(5, 20, 5):
    print(num, end=" ")

print("\n\n📗 Default Sequence (0 to 10, step=1):")
for num in number_sequence():
    print(num, end=" ")
