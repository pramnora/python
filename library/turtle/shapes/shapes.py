import turtle

#             COMPUTER: PC (home based)/OS: Linux Mint
# PROGRAMMING LANGUAGE: Python Version: 3.10.12/Editor: Nano 
#              PROGRAM: LOGO Turtle graphics/Create 'any' shape
# -------------------------------------------------------------
#              CREATED: Thu 100425 12:25 PM GMT 
#              UPDATED: Thu 100425 12:25 PM GMT

'''
 This program allows you to create 'any' shape...;
 in order to use it, effectively, 
 then, you just have to call the function: drawShape(arg1,arg2) using 2 arguments:
 - length, how long you wish the shape to be: small/medium/big
 - noOfSides, each side the shape has (eg. a triangle has 3 sides/a square 4 sides/and, so on...)
  ...after that is done; the program will calculate the rest for you: (360/noOfSides);
  as well as, draw the shape on screen so that you can view that shape.
'''

def drawShape(length,noOfSides):
    for drawEachSide in range(1,noOfSides+1):
        turtle.forward(length)
        turtle.left(360/noOfSides)

drawShape(100,3) # draws a triangle
drawShape(100,4) # draws a square 
drawShape(100,5) # draws a pentagon
