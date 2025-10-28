# Problem 11.2: Create three single-line text boxes using Tkinter

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("User Input Form")
root.geometry("400x250")

# Create labels and entry fields
tk.Label(root, text="Enter First Value:", font=("Arial", 12)).pack(pady=5)
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Value:", font=("Arial", 12)).pack(pady=5)
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

tk.Label(root, text="Enter Third Value:", font=("Arial", 12)).pack(pady=5)
entry3 = tk.Entry(root, width=30)
entry3.pack(pady=5)

# Function to display entered values
def show_values():
    val1 = entry1.get()
    val2 = entry2.get()
    val3 = entry3.get()
    print(f"Values entered: {val1}, {val2}, {val3}")

# Button to get values
tk.Button(root, text="Submit", command=show_values, font=("Arial", 12)).pack(pady=10)

# Run the GUI
root.mainloop()
