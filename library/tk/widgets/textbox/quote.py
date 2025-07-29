# This code is borrowed from:
# https://www.geeksforgeeks.org/python/python-tkinter-text-widget/

import tkinter as tk

root = tk.Tk()

# specify size of window.
root.geometry("250x170")

# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 52)

# Create label
l = tk.Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

Fact = """The sun shines every single day."""

# Here I've commented out b1...as it's NOT being used...
# Create button for next text.
# b1 = tk.Button(root, text = "Next", )

# Create an Exit button.
b2 = tk.Button(root, text = "Exit",
            command = root.destroy) 

l.pack()
T.pack()
# b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()
