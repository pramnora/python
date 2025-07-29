#----------------------------------------------------------------
#   PROGRAM: Adding 'buttons'/using pack()...
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
#   CREATED: 300520 06:09 AM GMT
#   UPDATED: 300520 06:09 AM GMT
#----------------------------------------------------------------
#      NOTE: How to create/use 4 buttons.../
#            which are each displayed using: pack()
#
#         1> Button 1/state=DISABLED (can't click)
#         2> Button 2/clickable...no response
#         3> Button 3/clickable...no response/with padding(x/y)
#         4> Button 4/clickable...borderwidth/response: message 
#----------------------------------------------------------------
# LATEST UPDATE: Tue 290725
#                It seems to me that this code is wrong...?!
#                It should say:
#                tk.Button()
#                tk.Label()
#                -(NOTE: I'm using Linux Mint OS.)-
# ---------------------------------------------------------------

# make call to import all: (*) from library: tkinter... 

from tkinter import *

root=Tk()       #...set root

#...rest of code goes inside here..

root.title("Buttons/pack()...")

#------------------------------------------------------------------------

myButton1 = Button(root,text="Click Me, I am disabled\ncan't even click!",state=DISABLED)
myButton1.pack()

#------------------------------------------------------------------------

myButton2 = Button(root,text="Click Me, I do not respond\nas I have no event attached")
myButton2.pack()

#------------------------------------------------------------------------

myButton3 = Button(root,text="Click Me, I do not respond\nas I have no event attached;\nalso, I am a padded button",padx=20,pady=20)
myButton3.pack()

#------------------------------------------------------------------------

def myClick():
    myLabel=Label(root,text="-Thanks, for clicking! ;-)")
    myLabel.pack()

myButton4 = Button(root,text="Click Me,\nI have a border going all around;\nI will respond with a text message.",borderwidth=10,command=myClick)
myButton4.pack()

#------------------------------------------------------------------------

root.mainloop() #...execute main loop...
