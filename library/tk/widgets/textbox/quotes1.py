# CREATED: Tue 29th July 2029 PM GMT
# UPDATED: Tue 29th July 2029 PM GMT
# ---------------------------------------------------------------
# This code borrowed from:
# https://www.geeksforgeeks.org/python/python-tkinter-text-widget/
# ----------------------------------------------------------------

import tkinter as tk     # import tk library
root = tk.Tk()           # create window
root.geometry("250x170") # specify size of window.

# ------------------------------------------------------------------

# variable declarations

facts=["sky is blue",
       "clouds are grey",
       "grass is green",
       "sun is yellow"]

n=0 # working variable used to change quotes

# ------------------------------------------------------------------

# create functions

def next():
    global n
    n = n + 1
    if n >= len(facts):
       n = 0
    showQuotes(n)

def showQuotes(n):
    T.delete("1.0","end")
    T.insert(tk.END, facts[n])

# ------------------------------------------------------------------

# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 52)

# Create label
l = tk.Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))
s
# Create an Exit button.
b1 = tk.Button(root, text = "Next",command=next)

# Create an Exit button.
b2 = tk.Button(root, text = "Exit",
            command = root.destroy) 
l.pack()
T.pack()
b1.pack()
b2.pack()

# ------------------------------------------------------------------

# Display quote
showQuotes(n)

tk.mainloop()
