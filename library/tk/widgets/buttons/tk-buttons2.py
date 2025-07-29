import tkinter as tk

root=tk.Tk()

root.title("Buttons...")

root.geometry("300x300") # set window width x height

def myButton1():
    print("Button1 clicked!")
    
def myButton2():
    print("Button2 clicked!")
    
def myButton3():
    print("Button3 clicked!")

button1=tk.Button(root,
                  text="Button 1",
                  command=myButton1,)

button1.pack(padx=10,pady=10)

button2=tk.Button(root,
                  text="Button 2",
                  command=myButton2)

button2.pack(padx=10,pady=10)

button3=tk.Button(root,
                  text="Button 3",
                  command=myButton3)

button3.pack(padx=10,pady=10)

root.mainloop()
