# import tkinter library

import tkinter as tk

# ---------------------------------------------------

# set window properties

root=tk.Tk()             # create window
root.title("Buttons...") # set window title text
root.geometry("160x160") # set window width x height

# ---------------------------------------------------

# Create functions for 3 separate buttons...;
# prints out a message when each button is clicked.

def myButton1():
    print("Button1 clicked!")
    
def myButton2():
    print("Button2 clicked!")
    
def myButton3():
    print("Button3 clicked!")

# ---------------------------------------------------

# Create 3 buttons... 

# set which window the button relates to (root)
# set the button text: text=""
# select which function is to run when the button is clicked: command=myFuncName

button1=tk.Button(root, text="Button 1",command=myButton1)
button2=tk.Button(root, text="Button 2",command=myButton2)
button3=tk.Button(root, text="Button 2",command=myButton3)

# add each button to window using pack()...which just means vertical placement...
# set the padding for each button: padx (x=horizontal)/pady (y=vertical) 

button1.pack(padx=10,pady=10)
button2.pack(padx=10,pady=10)
button3.pack(padx=10,pady=10)

# ---------------------------------------------------

root.mainloop() # create a window running loop
