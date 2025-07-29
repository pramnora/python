# CREATED: Tue 29th July 2029 PM GMT
# UPDATED: Tue 29th July 2029 PM GMT
# ---------------------------------------------------------------
# This code borrowed from:
# https://www.geeksforgeeks.org/python/python-tkinter-text-widget/
# ----------------------------------------------------------------

import tkinter as tk

root = tk.Tk()             # create window
root.title("TKInter: app") # set window title
root.geometry("380x260")   # specify size of window.

# --------------------------------------------------------------

# variable declarations

message="""
  AUTHOR: Mr. Paul Ramnora
   EMAIL: pramnora@yahoo.com
 -----------------------------------
COMPUTER: Home based PC
      OS: Linux Mint
LANGUAGE: Python 3
 LIBRARY: TKInter
 -----------------------------------
 CREATED: Tue 29th July 21:39 PM GMT
 UPDATED: Tue 29th July 21:39 PM GMT 
"""

# --------------------------------------------------------------

# Create text widget and specify size.
T = tk.Text(root, height = 12, width = 36)

# Create label
l = tk.Label(root, text = "About...")
l.config(font =("Courier", 14))

# Create an Exit button.
b1 = tk.Button(root, text = "Exit",command = root.destroy) 

l.pack()
T.pack()
b1.pack()

# --------------------------------------------------------------

# Display quote
T.insert(tk.END, message)

tk.mainloop()
