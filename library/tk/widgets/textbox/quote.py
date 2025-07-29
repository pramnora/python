# This code was originally borrowed from:
# https://www.geeksforgeeks.org/python/python-tkinter-text-widget/

# --------------------------------------------------------------- 

import tkinter as tk     # import TKInter library
root = tk.Tk()           # create window
root.geometry("250x170") # specify size of window.

# --------------------------------------------------------------- 

# Create text widget and specify size.
textbox1 = tk.Text(root, height = 5, width = 52)

# Create label
label1 = tk.Label(root, text = "Fact of the Day")
label1.config(font =("Courier", 14))

# Create an Exit button.
btn_exit = tk.Button(root, text = "Exit", command = root.destroy) 

# pack window components...stacking them vertically on top of one another...
label1.pack()
textbox1.pack()
btn_exit.pack()

# --------------------------------------------------------------- 

var_fact = "The sun shines every single day." # create variable
textbox1.insert(tk.END, var_fact)             # Insert The Fact.
tk.mainloop()                                 # run main window in a loop
