# Problem 11.1: Create a label and change its font style using Tkinter

import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Change Label Font Style")
root.geometry("400x200")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16, "bold"))
label.pack(pady=40)

# Create a function to change font style
def change_font():
    label.config(font=("Times New Roman", 20, "italic"))

# Button to change font
btn = tk.Button(root, text="Change Font", command=change_font, font=("Arial", 12))
btn.pack()

# Run the GUI event loop
root.mainloop()
