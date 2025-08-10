# ----------------------------------------------------------------------
# This code borrowed from:
# https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-combobox/

# CREATED: Sun 10 Aug 2025 18:19 PM GMT
# UPDATED: Sun 10 Aug 2025 18:19 PM GMT
# ----------------------------------------------------------------------

# import tkinter library
import tkinter as tk
# import ttk (combobox, is a part of ttk)
from tkinter import ttk
# set win name 
app = tk.Tk()
# set win size (widthxheight)
app.geometry("200x100")
# create label
labelTop = tk.Label(app, text="Choose your favourite month")
# position label using grid
labelTop.grid(column=0, row=0)
# create comboxbox
comboExample = ttk.Combobox(app, values=["January", "February", "March", "April"])
# print dictionary
print(dict(comboExample))
# position combobox
comboExample.grid(column=0, row=1)
# select which combobox option to display 
comboExample.current(1)
# display inside of terminal the selected combo box item 'index' number/item 'text' value
print(comboExample.current(), comboExample.get())
# execute window mainloop
app.mainloop()
