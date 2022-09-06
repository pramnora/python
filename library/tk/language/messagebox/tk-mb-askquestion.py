from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

result = messagebox.askquestion("Delete","Are you sure?",icon="warning")

if result=="yes":
   print("Deleted")
else:
   print("NOT deleted")
