#----------------------------------------------------------------
#   PROGRAM: Adding 'label' text using: grid()...
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
#   CREATED: 300520 05:05 AM GMT
#   UPDATED: 300520 05:05 AM GMT
#----------------------------------------------------------------
#      NOTE: How to create/use 4 x text labels...;
#            together with: grid().
#
#            grid(), works like using an Excel spreadsheet;
#            where there is a grid forming a series of rows/columns;
#            rows, go horizontally across;
#            and, columns go vertically both up and down;
#            so, there is row 1/column 1, column 2; -etc.
#            and, there is row 2/column 1, column 2; -etc.
#
#            The output of this code looks like the following:
#            Hello, world(1) Hello, world(2)
#            Hello, world(3) Hello, world(4)
#            ...which, in turn corresponds with...
#            grid(row=0,column=0) grid(row=0,column=1)
#            grid(row=1,column=0) grid(row=1,column=1)
#----------------------------------------------------------------

# make call to import all: (*) from library: tkinter... 

from tkinter import *

root=Tk()       #...set root

#...rest of code goes inside here..

root.title("Label/grid()...")

#------------------------------------------------------------------------

myLabel1 = Label(root,text="Hello, world(1)")
myLabel1.grid(row=0,column=0)

#------------------------------------------------------------------------

myLabel2 = Label(root,text="Hello, world(2)")
myLabel2.grid(row=0,column=1)

#------------------------------------------------------------------------

myLabel3 = Label(root,text="Hello, world(3)")
myLabel3.grid(row=1,column=0)

#------------------------------------------------------------------------

myLabel4 = Label(root,text="Hello, world(4)")
myLabel4.grid(row=1,column=1)

#------------------------------------------------------------------------

root.mainloop() #...execute main loop...
