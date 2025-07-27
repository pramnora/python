from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

result = messagebox.askokcancel("Delete","Delete all files?",icon="warning")

if result is True:
   print("All files deleted")
else:
   print("All files NOT deleted")
