#----------------------------------------------------------------
#   PROGRAM: Adding 'label' text using: pack()...
#  LANGUAGE: Python 3.8.2/(python.org)
#   LIBRARY: TKInter, used to build: GUI/Graphical User Interface
#  COMPUTER: Home based PC/OS: Windows 10 Professional
#    EDITOR: IDLE
#----------------------------------------------------------------
#    AUTHOR: Mr. Paul Ramnora
#     EMAIL: pramnora@yahoo.com
#  LOCATION: London, UK
# COPYRIGHT: (c)2020-, Mr. Paul Ramnora./All rights reserved.
#----------------------------------------------------------------
#   CREATED: 300520 04:27 AM GMT
#   UPDATED: 300520 04:27 AM GMT
#----------------------------------------------------------------
#      NOTE: How to create/use 4 x text labels...;
#            together with: pack().
#----------------------------------------------------------------

# make call to import all: (*) from library: tkinter... 

from tkinter import *

root=Tk()       #...set root

#...rest of code goes inside here..

root.title("Label/pack()...")

#------------------------------------------------------------------------

myLabel1 = Label(root,text="Hello, world!")
myLabel1.pack()

#------------------------------------------------------------------------

#...create a long text string message...;
#   which includes a number of line breaks: (\n)... 

strMsg  = "-(Congratulations,"
strMsg += "\nwe are learning"
strMsg += "\nhow to use,"
strMsg += "\nTKInter.)-"

# NOTE: padx - adds padding space going horizontally across(left/right)
#       pady - adds padding space going vertically (up/down)

myLabel2 = Label(root,text=strMsg,bg="black",fg="white",padx=10,pady=10)
myLabel2.pack()

#------------------------------------------------------------------------

myLabel3 = Label(root,text="Goodbye, world!")
myLabel3.pack()

#------------------------------------------------------------------------

strMsg="-(Press keys: [Alt] + [F4] to close this window.)-"

# bg - background/(background color)
# The first set of Hex digits is: FF/full (red)
# The second set of Hex digits is: FF/full (green)
# The third set of Hex digits is: 00/none (blue)
# (The mixture of both 'red/green' produces 'yellow';
#  so the background will be coloured: 'yellow'.)

strBackgroundColor="#FFFF00"

# fg - foreground/(text colour)
# The first set of Hex digits is: FF/full (red)
# The second set of Hex digits is: 00/none (green)
# The third set of Hex digits is: 00/none (blue)
# (So, the text will be coloured: 'red'.)

strForegroundColor="#FF0000"

myLabel4 = Label(root,text=strMsg,bg=strBackgroundColor,fg=strForegroundColor)
myLabel4.pack()

#------------------------------------------------------------------------

root.mainloop() #...execute main loop...
