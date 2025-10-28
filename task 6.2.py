# Problem 6.2: Count lines containing the word "ERROR"

def count_error_lines():
    count = 0
    with open("log.txt", "r") as file:
        for line in file:
            if "error" in line.lower():  # case-insensitive search
                count += 1
    print(f"⚙️ Number of lines containing 'ERROR': {count}")
    return count

# Run function
count_error_lines()
