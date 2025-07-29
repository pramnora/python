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

noOfQuotes=3-1
currentQuote=1-1

# create functions

def next():
    global currentQuote,noOfQuotes
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



