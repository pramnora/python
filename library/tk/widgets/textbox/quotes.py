# -----------------------------------------
#  PROGRAM: Display Quotes
# COMPUTER: Home based PC/Linux Mint OS
# LANGUAGE: Python 3
# -----------------------------------------
#  CREATED: Tue 29th July 2025 19:47 PM GMT
#  UPDATED: Tue 29th July 2025 19:47 PM GMT
# -----------------------------------------

# -------------------------------------------------------------------------------------

# NOTES

# This code was originally borrowed from...
# https://www.geeksforgeeks.org/python/python-tkinter-text-widget/
# -(Then, later on, adapted by me to suit my own specific purpose.)-

# Also, I had some help with learning how to clear text box contents...
# https://www.delftstack.com/howto/python-tkinter/how-to-clear-tkinter-text-box-widget/

# -------------------------------------------------------------------------------------

'''
WHAT THE PROGRAM DOES
This TKInter program...
displays a list of quotes
each of which is written into a text box...; 
together with a [Next] button...; 
so, that user can select what is the next quote. 
When the quotes reach the end...; 
then, the quotes start all over again 
going from the very beginning of the list. 
'''

import tkinter as tk

root = tk.Tk()

# specify size of window.
root.geometry("250x170")

# Create an array to store quotes

quotes=[
 "One",
 "Two",
 "Three" 
]

currentQuote=1-1

# create functions

def next():
    global currentQuote
    if (currentQuote < len(quotes)-1):
       currentQuote+=1
    else: 
       currentQuote=0     
    showQuote(currentQuote)

def showQuote(n):
    T.delete("1.0","end")
    T.insert(tk.END, quotes[n])
    

# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 52)

# Create label
l = tk.Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

# Create button for next text.
b1 = tk.Button(root, text = "Next", command=next)

# Create an Exit button.
b2 = tk.Button(root, text = "Exit",
            command = root.destroy) 

l.pack()
T.pack()
b1.pack()
b2.pack()

# Show currently selected quote
showQuote(currentQuote)

tk.mainloop()



