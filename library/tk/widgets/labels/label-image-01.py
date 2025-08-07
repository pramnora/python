# -----------------------------------------------------
# This program allows the user to select an image file;
# and, display it using TKInter + PIL 
# -----------------------------------------------------
# (NOTE: I used AI: 
#        https://copilot.microsoft.com
#        ...to help me figure this code out.)
# -----------------------------------------------------

import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
root.title("Image Viewer")

image_path="self-portrait.jpg"
image=Image.open(image_path)

image=image.resize((400,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)

label=tk.Label(root,image=photo)
label.pack()

root.mainloop()
