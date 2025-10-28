# Problem 6.1: Write a sentence into log.txt

def write_to_log():
    text = ("Error objects are thrown when runtime errors occur. "
            "The Error object can also be used as a base object for user-defined exceptions.")
    
    with open("log.txt", "w") as file:
        file.write(text)
    
    print("✅ log.txt created and sentence written successfully.")

# Run function
write_to_log()
